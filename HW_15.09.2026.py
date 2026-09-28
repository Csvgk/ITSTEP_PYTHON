import threading
import time
import random

#1
def count_up():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)


def count_down():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(0.5)


t1 = threading.Thread(target=count_up)
t2 = threading.Thread(target=count_down)

t1.start()
t2.start()

t1.join()
t2.join()

print("Обидва потоки завершено")

#2
def download_file(filename, duration):
    print(f"Початок завантаження {filename}")
    time.sleep(duration)
    print(f"{filename} завантажено")


files = [
    ("photo.jpg", 2),
    ("video.mp4", 3),
    ("document.pdf", 1),
]

threads = []
for filename, duration in files:
    thread = threading.Thread(target=download_file, args=(filename, duration))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Усі файли завантажено!")

#3
def runner(name, pass_verb, finish_verb):
    for stage in range(1, 6):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{name} {pass_verb} етап {stage}")
    print(f"{name} {finish_verb}!")


athletes = [
    ("Олег", "пройшов", "фінішував"),
    ("Анна", "пройшла", "фінішувала"),
    ("Максим", "пройшов", "фінішував"),
]

threads = [threading.Thread(target=runner, args=athlete) for athlete in athletes]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

#4
def sum_range(start, end, result, index):
    total = sum(range(start, end + 1))
    print(f"Сума чисел від {start} до {end}: {total}")
    result[index] = total


start1 = int(input("Введіть початок першого діапазону: "))
end1 = int(input("Введіть кінець першого діапазону: "))
start2 = int(input("Введіть початок другого діапазону: "))
end2 = int(input("Введіть кінець другого діапазону: "))

results = [None, None]

t1 = threading.Thread(target=sum_range, args=(start1, end1, results, 0))
t2 = threading.Thread(target=sum_range, args=(start2, end2, results, 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("Обчислення завершено.")

#5
def cook_order(name, duration):
    print(f"Починаємо готувати {name}")
    time.sleep(duration)
    print(f"{name} готово!")


orders = [
    ("Pizza", 4),
    ("Coffee", 2),
    ("Burger", 3),
    ("Pasta", 5),
]

threads = [threading.Thread(target=cook_order, args=(name, duration)) for name, duration in orders]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Усі замовлення готові!")

#6
def deliver_order(courier_name):
    stages = [
        "отримав замовлення",
        "забрав замовлення",
        "їде до клієнта",
        "замовлення доставлено",
    ]
    for stage in stages:
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{courier_name}: {stage}")


couriers = ["Courier 1", "Courier 2", "Courier 3"]

start_time = time.time()

threads = [threading.Thread(target=deliver_order, args=(courier,)) for courier in couriers]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("=== УСІ ЗАМОВЛЕННЯ ДОСТАВЛЕНО ===")
print(f"Час виконання з потоками: {time.time() - start_time:.2f} с")

start_time = time.time()

for courier in couriers:
    deliver_order(courier)

print(f"Час виконання без потоків: {time.time() - start_time:.2f} с")