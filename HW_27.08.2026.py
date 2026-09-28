#1
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass

    def show_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")


class Programmer(Employee):
    def work(self):
        print(f"{self.name} пише код")

    def calculate_bonus(self):
        return self.salary * 0.15


class Designer(Employee):
    def work(self):
        print(f"{self.name} створює дизайн")

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def work(self):
        print(f"{self.name} керує командою")

    def calculate_bonus(self):
        return self.salary * 0.20


employees = [
    Programmer("Max", 30000),
    Designer("Anna", 25000),
    Manager("Ivan", 40000),
]

for emp in employees:
    emp.show_info()
    emp.work()
    print(f"Бонус: {emp.calculate_bonus()}")
    print()

#2
from abc import ABC, ABCMeta


class ValidationMeta(ABCMeta):
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if callable(value) and not key.startswith("__") and not key.startswith("do_"):
                raise ValueError(f"Клас '{name}' порушує правило: метод '{key}' повинен починатися з 'do_'")
        if "description" not in namespace:
            namespace["description"] = "No description provided"
        elif not isinstance(namespace["description"], str):
            raise ValueError(f"Клас '{name}' порушує правило: атрибут 'description' повинен бути рядком")
        return super().__new__(mcs, name, bases, namespace)


class ValidatedClass(ABC, metaclass=ValidationMeta):
    pass


print("-" * 10)

try:
    class GoodClass(ValidatedClass):
        description = "Правильний клас з методами do_"

        def do_task(self):
            print("Виконую задачу")

        def do_something_else(self):
            print("Виконую ще щось")
    print("Клас GoodClass успішно створено")
except ValueError as e:
    print(f"Помилка створення класу GoodClass: {e}")

try:
    class BadClass(ValidatedClass):
        def task(self):
            print("Виконую задачу")
    print("Клас BadClass успішно створено")
except ValueError as e:
    print(f"Помилка створення класу BadClass: {e}")

try:
    class NoDescriptionClass(ValidatedClass):
        def do_work(self):
            print("Роблю роботу")
    print("Клас NoDescriptionClass успішно створено")
except ValueError as e:
    print(f"Помилка створення класу NoDescriptionClass: {e}")

print()
good = GoodClass()
good.do_task()
print(good.description)

print()
no_desc = NoDescriptionClass()
no_desc.do_work()
print(no_desc.description)