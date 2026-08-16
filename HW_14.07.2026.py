#1
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Python", "Java")

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Заміну виконано.")

#2
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("char_count.txt", "w", encoding="utf-8") as f:
    for i, line in enumerate(lines, start=1):
        count = len(line.rstrip("\n"))
        f.write(f"Рядок {i}: {count} символів\n")

print("Підрахунок завершено. Результат у char_count.txt")

#3
with open("old_version.txt", "r", encoding="utf-8") as f:
    old_lines = set(line.rstrip("\n") for line in f)

with open("new_version.txt", "r", encoding="utf-8") as f:
    new_lines = set(line.rstrip("\n") for line in f)

only_in_old = old_lines - new_lines
only_in_new = new_lines - old_lines

with open("differences.txt", "w", encoding="utf-8") as f:
    f.write("Рядки, які є тільки в old_version.txt:\n")
    for line in sorted(only_in_old):
        f.write(line + "\n")

    f.write("\nРядки, які є тільки в new_version.txt:\n")
    for line in sorted(only_in_new):
        f.write(line + "\n")

print("Порівняння завершено. Результат у differences.txt")

#4
with open("words.txt", "r", encoding="utf-8") as f:
    banned_words = [word.strip() for word in f if word.strip()]

with open("source.txt", "r", encoding="utf-8") as f:
    text = f.read()

for word in banned_words:
    text = text.replace(word, "***")

with open("censored.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Цензурування завершено. Результат у censored.txt")

#5
ORDERS_FILE = "orders.txt"

def load_orders():
    orders = {}
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        number, product, quantity, price = parts
                        orders[number] = {
                            "product": product,
                            "quantity": quantity,
                            "price": price
                        }
    except FileNotFoundError:
        pass
    return orders

def save_orders(orders):
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        for number, data in orders.items():
            f.write(f"{number}|{data['product']}|{data['quantity']}|{data['price']}\n")

def add_order(orders):
    number = input("Номер замовлення: ").strip()
    if number in orders:
        print("Замовлення з таким номером вже існує.")
        return
    product = input("Назва товару: ").strip()
    quantity = input("Кількість: ").strip()
    price = input("Ціна: ").strip()
    orders[number] = {"product": product, "quantity": quantity, "price": price}
    save_orders(orders)
    print("Замовлення додано.")

def view_orders(orders):
    if not orders:
        print("Замовлень немає.")
        return
    print("\n--- Усі замовлення ---")
    for number, data in orders.items():
        print(f"№{number}: {data['product']}, кількість: {data['quantity']}, ціна: {data['price']}")
    print()

def search_order(orders):
    number = input("Введіть номер замовлення: ").strip()
    if number in orders:
        data = orders[number]
        print(f"№{number}: {data['product']}, кількість: {data['quantity']}, ціна: {data['price']}")
    else:
        print("Замовлення не знайдено.")

def update_order(orders):
    number = input("Введіть номер замовлення: ").strip()
    if number not in orders:
        print("Замовлення не знайдено.")
        return
    quantity = input("Нова кількість: ").strip()
    price = input("Нова ціна: ").strip()
    orders[number]["quantity"] = quantity
    orders[number]["price"] = price
    save_orders(orders)
    print("Замовлення оновлено.")

def delete_order(orders):
    number = input("Введіть номер замовлення: ").strip()
    if number in orders:
        del orders[number]
        save_orders(orders)
        print("Замовлення видалено.")
    else:
        print("Замовлення не знайдено.")

def main():
    orders = load_orders()
    while True:
        print("\n===== Меню замовлень =====")
        print("1. Додати нове замовлення")
        print("2. Переглянути всі замовлення")
        print("3. Пошук замовлення за номером")
        print("4. Оновити замовлення")
        print("5. Видалити замовлення")
        print("6. Вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            add_order(orders)
        elif choice == "2":
            view_orders(orders)
        elif choice == "3":
            search_order(orders)
        elif choice == "4":
            update_order(orders)
        elif choice == "5":
            delete_order(orders)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#6
STUDENTS_FILE = "students.txt"

def load_students():
    students = {}
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        name, course, average = parts
                        students[name] = {
                            "course": course,
                            "average": average
                        }
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        for name, data in students.items():
            f.write(f"{name}|{data['course']}|{data['average']}\n")

def add_student(students):
    name = input("Ім'я студента: ").strip()
    if name in students:
        print("Студент з таким ім'ям вже існує.")
        return
    course = input("Курс: ").strip()
    average = input("Середній бал: ").strip()
    students[name] = {"course": course, "average": average}
    save_students(students)
    print("Студента додано.")

def view_students(students):
    if not students:
        print("Студентів немає.")
        return
    print("\n--- Усі студенти ---")
    for name, data in students.items():
        print(f"{name}: курс {data['course']}, середній бал {data['average']}")
    print()

def search_student(students):
    name = input("Введіть ім'я студента: ").strip()
    if name in students:
        data = students[name]
        print(f"{name}: курс {data['course']}, середній бал {data['average']}")
    else:
        print("Студента не знайдено.")

def update_student(students):
    name = input("Введіть ім'я студента: ").strip()
    if name not in students:
        print("Студента не знайдено.")
        return
    course = input("Новий курс: ").strip()
    average = input("Новий середній бал: ").strip()
    students[name]["course"] = course
    students[name]["average"] = average
    save_students(students)
    print("Дані студента оновлено.")

def delete_student(students):
    name = input("Введіть ім'я студента: ").strip()
    if name in students:
        del students[name]
        save_students(students)
        print("Студента видалено.")
    else:
        print("Студента не знайдено.")

def main():
    students = load_students()
    while True:
        print("\n===== Меню студентів =====")
        print("1. Додати нового студента")
        print("2. Переглянути всіх студентів")
        print("3. Пошук студента за ім'ям")
        print("4. Оновити дані студента")
        print("5. Видалити студента")
        print("6. Вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()