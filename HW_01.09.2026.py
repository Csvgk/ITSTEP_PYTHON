#1
class Node:
    def __init__(self, city):
        self.city = city
        self.next = None


city1 = Node("Київ")
city2 = Node("Львів")
city3 = Node("Одеса")
city4 = Node("Харків")

city1.next = city2
city2.next = city3
city3.next = city4

print(city1.city)
print(city1.next.city)
print(city1.next.next.city)
print(city1.next.next.next.city)

#2
class NumberNode:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = NumberNode(10)
node2 = NumberNode(25)
node3 = NumberNode(40)
node4 = NumberNode(55)
node5 = NumberNode(70)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1
count = 0
while current is not None:
    print(current.value)
    count += 1
    current = current.next

print(f"Кількість вузлів: {count}")

#3
class MovieNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MovieLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = MovieNode(data)
        new_node.next = self.head
        self.head = new_node

    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


# Я думаю, що результат буде:
# Titanic
# Avatar
# Dune
# Interstellar
movies = MovieLinkedList()
movies.add_first("Interstellar")
movies.add_first("Dune")
movies.add_first("Avatar")
movies.add_first("Titanic")

movies.show()

#4
class StudentNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = StudentNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False


students = StudentLinkedList()
students.add_last("Анна")
students.add_last("Максим")
students.add_last("Ірина")
students.add_last("Олексій")
students.add_last("Марія")

print(students.contains("Ірина"))
print(students.contains("Денис"))

search_name = input("Введіть ім'я для пошуку: ")
print(students.contains(search_name))

#5
class SongNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class PlaylistLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = SongNode(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = SongNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def count(self):
        current = self.head
        total = 0
        while current is not None:
            total += 1
            current = current.next
        return total

    def contains(self, song):
        current = self.head
        while current is not None:
            if current.data == song:
                return True
            current = current.next
        return False


playlist = PlaylistLinkedList()
playlist.add_last("Numb")
playlist.add_last("Believer")
playlist.add_last("Take On Me")
playlist.add_last("Zombie")
playlist.add_last("Thunder")

print("Плейлист:")
playlist.show()
print(f"Кількість пісень: {playlist.count()}")

playlist.add_first("In The End")
playlist.add_last("Faded")

print("\nОновлений плейлист:")
playlist.show()

print(playlist.contains("Zombie"))
print(playlist.contains("Unknown Song"))

#6
class WagonNode:
    def __init__(self, number):
        self.number = number
        self.next = None


class Train:
    def __init__(self):
        self.head = None

    def add_wagon(self, number):
        new_node = WagonNode(number)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def show_train(self):
        current = self.head
        result = ""
        while current is not None:
            result += f"[{current.number}] -> "
            current = current.next
        result += "None"
        print(result)

    def count_wagons(self):
        current = self.head
        total = 0
        while current is not None:
            total += 1
            current = current.next
        return total

    def find_wagon(self, number):
        current = self.head
        while current is not None:
            if current.number == number:
                return True
            current = current.next
        return False


train = Train()
train.add_wagon(1)
train.add_wagon(2)
train.add_wagon(3)
train.add_wagon(4)
train.add_wagon(5)

train.show_train()
print(train.count_wagons())
print(train.find_wagon(3))
print(train.find_wagon(10))

#Бонус
class NumNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class NumberLinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = NumNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def show(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def replace(self, old_value, new_value):
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next
        print("Елемент не знайдено")


numbers = NumberLinkedList()
numbers.add_last(10)
numbers.add_last(20)
numbers.add_last(30)
numbers.add_last(40)

numbers.show()
numbers.replace(30, 100)
numbers.show()
numbers.replace(999, 1)