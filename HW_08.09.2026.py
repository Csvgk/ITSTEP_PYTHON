import heapq
import random
from collections import deque
from datetime import datetime

#1
class Request:
    def __init__(self, priority, client_name):
        self.priority = priority
        self.client_name = client_name
        self.timestamp = datetime.now().strftime("%H:%M:%S")


class RequestQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
        self.statistics = []

    def add_request(self, client_name, priority):
        self.counter += 1
        request = Request(priority, client_name)
        heapq.heappush(self.queue, (priority, self.counter, request))
        print(f"Клієнт {client_name} доданий у чергу з пріоритетом {priority}")

    def process_request(self):
        if not self.queue:
            print("Черга запитів порожня")
            return
        priority, _, request = heapq.heappop(self.queue)
        self.statistics.append((request.client_name, request.timestamp))
        print(f"Оброблено запит клієнта {request.client_name} (пріоритет {priority})")

    def show_statistics(self):
        print("Статистика оброблених запитів:")
        for client_name, timestamp in self.statistics:
            print(f"{client_name} - {timestamp}")


server = RequestQueue()
server.add_request("Клієнт A", 3)
server.add_request("Клієнт B", 1)
server.add_request("Клієнт C", 2)

server.process_request()
server.process_request()
server.process_request()
server.process_request()

server.show_statistics()

#2
class Passenger:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time


class Pier:
    def __init__(self, passenger_intervals, boat_intervals, stop_type, simulation_time):
        self.passenger_intervals = passenger_intervals
        self.boat_intervals = boat_intervals
        self.stop_type = stop_type
        self.simulation_time = simulation_time

        self.waiting_queue = deque()
        self.events = []
        self.wait_times = []
        self.max_waiting_count = 0

    def get_interval(self, intervals, current_time):
        hour = int(current_time // 60) % 24
        for start, end, avg_interval in intervals:
            if start <= hour < end:
                return random.expovariate(1 / avg_interval)
        return random.expovariate(1 / intervals[-1][2])

    def run(self):
        heapq.heappush(self.events, (self.get_interval(self.passenger_intervals, 0), "passenger"))
        heapq.heappush(self.events, (self.get_interval(self.boat_intervals, 0), "boat"))

        while self.events:
            current_time, event_type = heapq.heappop(self.events)
            if current_time > self.simulation_time:
                break

            if event_type == "passenger":
                passenger = Passenger(current_time)
                self.waiting_queue.append(passenger)
                self.max_waiting_count = max(self.max_waiting_count, len(self.waiting_queue))
                next_time = current_time + self.get_interval(self.passenger_intervals, current_time)
                heapq.heappush(self.events, (next_time, "passenger"))

            elif event_type == "boat":
                free_seats = random.randint(5, 20)
                boarded = 0
                while self.waiting_queue and boarded < free_seats:
                    passenger = self.waiting_queue.popleft()
                    self.wait_times.append(current_time - passenger.arrival_time)
                    boarded += 1
                print(f"Час {current_time:.1f} хв: катер забрав {boarded} пасажирів, вільних місць залишилось {free_seats - boarded}")
                next_time = current_time + self.get_interval(self.boat_intervals, current_time)
                heapq.heappush(self.events, (next_time, "boat"))

    def average_wait_time(self):
        if not self.wait_times:
            return 0
        return sum(self.wait_times) / len(self.wait_times)

    def sufficient_boat_interval(self, max_people):
        avg_passenger_interval = sum(interval for _, _, interval in self.passenger_intervals) / len(self.passenger_intervals)
        return max_people * avg_passenger_interval


random.seed(42)

passenger_intervals = [
    (0, 6, 20),
    (6, 9, 3),
    (9, 17, 8),
    (17, 20, 3),
    (20, 24, 15),
]

boat_intervals = [
    (0, 6, 40),
    (6, 9, 10),
    (9, 17, 15),
    (17, 20, 10),
    (20, 24, 30),
]

pier = Pier(passenger_intervals, boat_intervals, "кінцева", simulation_time=300)
pier.run()

max_people = 15
print(f"Тип зупинки: {pier.stop_type}")
print(f"Середній час очікування пасажира: {pier.average_wait_time():.2f} хв")
print(f"Максимальна кількість людей одночасно на зупинці: {pier.max_waiting_count}")
print(f"Достатній інтервал між катерами для не більше {max_people} людей: {pier.sufficient_boat_interval(max_people):.2f} хв")

#3
class Dictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, word, translations=None):
        if word in self.words:
            print(f"Слово '{word}' вже існує")
            return
        self.words[word] = {"translations": translations or [], "count": 0}
        print(f"Слово '{word}' додано")

    def remove_word(self, word):
        if word not in self.words:
            print(f"Слово '{word}' не знайдено")
            return
        del self.words[word]
        print(f"Слово '{word}' видалено")

    def update_word(self, old_word, new_word):
        if old_word not in self.words:
            print(f"Слово '{old_word}' не знайдено")
            return
        self.words[new_word] = self.words.pop(old_word)
        print(f"Слово '{old_word}' перейменовано на '{new_word}'")

    def add_translation(self, word, translation):
        if word not in self.words:
            print(f"Слово '{word}' не знайдено")
            return
        self.words[word]["translations"].append(translation)
        print(f"Переклад '{translation}' додано до слова '{word}'")

    def remove_translation(self, word, translation):
        if word not in self.words or translation not in self.words[word]["translations"]:
            print("Такого перекладу не знайдено")
            return
        self.words[word]["translations"].remove(translation)
        print(f"Переклад '{translation}' видалено зі слова '{word}'")

    def update_translation(self, word, old_translation, new_translation):
        if word not in self.words or old_translation not in self.words[word]["translations"]:
            print("Такого перекладу не знайдено")
            return
        index = self.words[word]["translations"].index(old_translation)
        self.words[word]["translations"][index] = new_translation
        print(f"Переклад оновлено: '{old_translation}' -> '{new_translation}'")

    def show_word(self, word):
        if word not in self.words:
            print(f"Слово '{word}' не знайдено")
            return
        self.words[word]["count"] += 1
        translations = ", ".join(self.words[word]["translations"])
        print(f"{word}: {translations}")

    def show_top_popular(self, n=10):
        sorted_words = sorted(self.words.items(), key=lambda item: item[1]["count"], reverse=True)
        print(f"Топ-{n} найпопулярніших слів:")
        for word, data in sorted_words[:n]:
            print(f"{word} - {data['count']} звернень")

    def show_top_unpopular(self, n=10):
        sorted_words = sorted(self.words.items(), key=lambda item: item[1]["count"])
        print(f"Топ-{n} найнепопулярніших слів:")
        for word, data in sorted_words[:n]:
            print(f"{word} - {data['count']} звернень")


dictionary = Dictionary()
dictionary.add_word("hello", ["hola"])
dictionary.add_word("world", ["mundo"])
dictionary.add_word("cat", ["gato"])
dictionary.add_word("dog", ["perro"])
dictionary.add_word("house", ["casa"])

dictionary.show_word("hello")
dictionary.show_word("hello")
dictionary.show_word("world")

dictionary.add_translation("cat", "gatito")
dictionary.update_translation("dog", "perro", "can")
dictionary.remove_translation("house", "casa")
dictionary.add_translation("house", "hogar")

dictionary.show_top_popular(3)
dictionary.show_top_unpopular(3)

#4
class FineDatabase:
    def __init__(self):
        self.people = {}

    def add_person(self, code, name, city):
        if code in self.people:
            print(f"Особа з кодом {code} вже існує")
            return
        self.people[code] = {"name": name, "city": city, "fines": []}
        print(f"Особу {name} додано")

    def add_fine(self, code, fine_type, amount):
        if code not in self.people:
            print(f"Особу з кодом {code} не знайдено")
            return
        self.people[code]["fines"].append({"type": fine_type, "amount": amount})
        print(f"Штраф '{fine_type}' на суму {amount} додано для коду {code}")

    def remove_fine(self, code, fine_type):
        if code not in self.people:
            print(f"Особу з кодом {code} не знайдено")
            return
        fines = self.people[code]["fines"]
        for fine in fines:
            if fine["type"] == fine_type:
                fines.remove(fine)
                print(f"Штраф '{fine_type}' видалено для коду {code}")
                return
        print(f"Штраф '{fine_type}' не знайдено")

    def replace_person(self, code, name, city, fines):
        if code not in self.people:
            print(f"Особу з кодом {code} не знайдено")
            return
        self.people[code] = {"name": name, "city": city, "fines": fines}
        print(f"Дані для коду {code} оновлено")

    def print_all(self):
        print("Повна база даних:")
        for code, data in self.people.items():
            self._print_person(code, data)

    def print_by_code(self, code):
        if code not in self.people:
            print(f"Особу з кодом {code} не знайдено")
            return
        self._print_person(code, self.people[code])

    def print_by_fine_type(self, fine_type):
        print(f"Штрафи типу '{fine_type}':")
        for code, data in self.people.items():
            for fine in data["fines"]:
                if fine["type"] == fine_type:
                    print(f"{data['name']} (код {code}): {fine['amount']}")

    def print_by_city(self, city):
        print(f"Особи з міста {city}:")
        for code, data in self.people.items():
            if data["city"] == city:
                self._print_person(code, data)

    def _print_person(self, code, data):
        print(f"Код: {code}, Ім'я: {data['name']}, Місто: {data['city']}")
        for fine in data["fines"]:
            print(f"  - {fine['type']}: {fine['amount']}")


db = FineDatabase()
db.add_person("100", "Іван Петренко", "Київ")
db.add_person("200", "Марія Коваль", "Львів")
db.add_person("300", "Олег Сидоренко", "Київ")

db.add_fine("100", "Перевищення швидкості", 500)
db.add_fine("100", "Паркування", 200)
db.add_fine("200", "Перевищення швидкості", 700)
db.add_fine("300", "Паркування", 150)

db.print_all()
db.print_by_code("100")
db.print_by_fine_type("Паркування")
db.print_by_city("Київ")

db.remove_fine("100", "Паркування")
db.print_by_code("100")

db.replace_person("200", "Марія Коваленко", "Одеса", [{"type": "Несплата податку", "amount": 1000}])
db.print_by_code("200")