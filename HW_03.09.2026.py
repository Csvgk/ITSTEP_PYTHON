class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return self.items == []


#1
# Box 5 буде розвантажена першою, бо стек працює за принципом LIFO
# (Last In - First Out): останній елемент, який поклали в стек,
# виймається з нього першим.
truck = Stack()
truck.push("Box 1")
truck.push("Box 2")
truck.push("Box 3")
truck.push("Box 4")
truck.push("Box 5")

while not truck.is_empty():
    box = truck.pop()
    print(f"Розвантажено: {box}")

print("Вантажівка порожня")

#2
text = input("Введіть текст: ")

reverse_stack = Stack()
for char in text:
    reverse_stack.push(char)

reversed_text = ""
while not reverse_stack.is_empty():
    reversed_text += reverse_stack.pop()

print(reversed_text)

clean_text = text.lower().replace(" ", "")

palindrome_stack = Stack()
for char in clean_text:
    palindrome_stack.push(char)

reversed_clean = ""
while not palindrome_stack.is_empty():
    reversed_clean += palindrome_stack.pop()

if clean_text == reversed_clean:
    print(f"{text} → паліндром")
else:
    print(f"{text} → не паліндром")

#3
class Parking:
    def __init__(self, max_cars):
        self.cars = Stack()
        self.max_cars = max_cars

    def park(self, car):
        if self.is_full():
            print("Парковка заповнена")
            return
        self.cars.push(car)
        print(f"Автомобіль {car} заїхав на парковку")

    def leave(self):
        car = self.cars.pop()
        if car is None:
            print("Парковка порожня")
            return
        print(f"Автомобіль {car} виїхав з парковки")

    def last_car(self):
        car = self.cars.peek()
        if car is None:
            print("Парковка порожня")
            return
        print(f"Наступним виїде: {car}")

    def is_full(self):
        return len(self.cars.items) >= self.max_cars

    def show_count(self):
        print(f"Кількість автомобілів: {len(self.cars.items)}")


parking = Parking(3)
parking.park("BMW")
parking.park("Audi")
parking.park("Tesla")
parking.park("Toyota")

parking.show_count()
parking.last_car()

parking.leave()
parking.last_car()
parking.show_count()


class ActionHistory:
    def __init__(self):
        self.actions = Stack()

    def add_action(self, action):
        self.actions.push(action)
        print(f"Додано: {action}")

    def undo(self):
        last_action = self.actions.pop()
        if last_action is None:
            print("Немає дій для скасування")
            return
        print(f"Скасовано: {last_action}")
        top = self.actions.peek()
        if top is not None:
            print(f"Новою вершиною є: {top}")


history = ActionHistory()
history.add_action("Додано текст")
history.add_action("Змінено колір")
history.add_action("Додано зображення")

history.undo()
history.undo()
history.undo()
history.undo()