#1
import json

student = {
    "name": "Іван",
    "age": 20,
    "city": "Київ",
    "group": "ПЗ-23"
}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=4)

with open("student.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Ім'я: {data['name']}")
print(f"Вік: {data['age']}")
print(f"Місто: {data['city']}")
print(f"Група: {data['group']}")

#2
import csv

products = []
print("Введіть інформацію про 5 товарів:")
for i in range(5):
    print(f"\nТовар {i + 1}:")
    name = input("Назва: ")
    price = float(input("Ціна: "))
    quantity = int(input("Кількість: "))
    products.append([name, price, quantity])

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Назва", "Ціна", "Кількість"])
    writer.writerows(products)

print("\n--- Товари ---")
with open("products.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]:<20} {row[1]:<10} {row[2]:<10}")

#3
FILENAME = "movies.json"

def load_movies():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return eval(content)
    except:
        return []

def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("[\n")
        for i, m in enumerate(movies):
            title = m["title"].replace('"', '\\"')
            genre = m["genre"].replace('"', '\\"')
            f.write("  {\n")
            f.write(f'    "title": "{title}",\n')
            f.write(f'    "genre": "{genre}",\n')
            f.write(f'    "year": {m["year"]},\n')
            f.write(f'    "rating": {m["rating"]}\n')
            f.write("  }")
            if i < len(movies) - 1:
                f.write(",")
            f.write("\n")
        f.write("]\n")

def add_movie(movies):
    title = input("Назва фільму: ")
    genre = input("Жанр: ")
    year = int(input("Рік: "))
    rating = float(input("Рейтинг: "))
    movies.append({
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating
    })
    save_movies(movies)
    print("Фільм додано!")

def show_all(movies):
    if not movies:
        print("Каталог порожній.")
        return
    print("\n--- Усі фільми ---")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m['title']} | {m['genre']} | {m['year']} | {m['rating']}")

def find_by_genre(movies):
    genre = input("Введіть жанр: ").lower()
    found = [m for m in movies if m["genre"].lower() == genre]
    if found:
        print(f"\nФільми жанру '{genre}':")
        for m in found:
            print(f"- {m['title']} ({m['year']}) — {m['rating']}")
    else:
        print("Фільмів такого жанру не знайдено.")

def delete_movie(movies):
    show_all(movies)
    if not movies:
        return
    try:
        idx = int(input("Номер фільму для видалення: ")) - 1
        if 0 <= idx < len(movies):
            deleted = movies.pop(idx)
            save_movies(movies)
            print(f"Фільм '{deleted['title']}' видалено.")
        else:
            print("Невірний номер.")
    except ValueError:
        print("Введіть число.")

def main():
    movies = load_movies()
    while True:
        print("\n=== Каталог фільмів ===")
        print("1. Додати фільм")
        print("2. Показати всі фільми")
        print("3. Знайти фільми за жанром")
        print("4. Видалити фільм")
        print("5. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            show_all(movies)
        elif choice == "3":
            find_by_genre(movies)
        elif choice == "4":
            delete_movie(movies)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()

#4
import csv

FILENAME = "grades.csv"
FIELDNAMES = ["ПІБ", "Група", "Оцінка"]

def load_students():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except:
        return []

def save_students(students):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

def add_student(students):
    name = input("ПІБ: ")
    group = input("Група: ")
    grade = float(input("Оцінка: "))
    students.append({
        "ПІБ": name,
        "Група": group,
        "Оцінка": str(grade)
    })
    save_students(students)
    print("Студента додано!")

def show_all(students, sort=True):
    if not students:
        print("Журнал порожній.")
        return
    if sort:
        students = sorted(students, key=lambda x: float(x["Оцінка"]), reverse=True)
    print("\n--- Усі студенти ---")
    print(f"{'ПІБ':<30} {'Група':<12} {'Оцінка':<8}")
    print("-" * 50)
    for s in students:
        print(f"{s['ПІБ']:<30} {s['Група']:<12} {s['Оцінка']:<8}")

def find_student(students):
    name = input("Введіть ПІБ (або частину): ").lower()
    found = [s for s in students if name in s["ПІБ"].lower()]
    if found:
        print("\nЗнайдені студенти:")
        for s in found:
            print(f"{s['ПІБ']} | {s['Група']} | {s['Оцінка']}")
    else:
        print("Студента не знайдено.")

def average_group(students):
    group = input("Введіть групу: ")
    group_students = [s for s in students if s["Група"] == group]
    if group_students:
        avg = sum(float(s["Оцінка"]) for s in group_students) / len(group_students)
        print(f"Середній бал групи {group}: {avg:.2f}")
    else:
        print("Студентів цієї групи не знайдено.")

def show_above_90(students):
    high = [s for s in students if float(s["Оцінка"]) > 90]
    if high:
        high = sorted(high, key=lambda x: float(x["Оцінка"]), reverse=True)
        print("\nСтуденти з балом > 90:")
        for s in high:
            print(f"{s['ПІБ']} | {s['Група']} | {s['Оцінка']}")
    else:
        print("Немає студентів з балом більше 90.")

def main():
    students = load_students()
    while True:
        print("\n=== Журнал оцінок ===")
        print("1. Додати студента")
        print("2. Показати всіх студентів")
        print("3. Знайти студента")
        print("4. Обчислити середній бал групи")
        print("5. Показати студентів із балом більше 90")
        print("6. Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            average_group(students)
        elif choice == "5":
            show_above_90(students)
        elif choice == "6":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()