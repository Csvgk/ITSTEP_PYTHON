#1
capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}

print("Країни:", list(capitals.keys()))

print("Столиці:", list(capitals.values()))

capitals["Франція"] = "Париж"
print("Оновлений словник:", capitals)

#2
prices = {"яблуко": 15, "банан": 20, "груша": 18}

product = input("Введіть назву товару: ").strip().lower()

if product in prices:
    print(f"Ціна товару '{product}': {prices[product]} грн")
else:
    print("Такого товару немає в магазині.")

#3
employees = {}


def add_employee():
    name = input("ПІБ: ").strip()
    phone = input("Телефон: ").strip()
    email = input("Корпоративний email: ").strip()
    position = input("Посада: ").strip()
    office = input("Номер кабінету: ").strip()
    skype = input("Skype: ").strip()

    employees[name] = {
        "телефон": phone,
        "email": email,
        "посада": position,
        "кабінет": office,
        "skype": skype
    }
    print(f"Працівника {name} додано.")


def delete_employee():
    name = input("Введіть ПІБ для видалення: ").strip()
    if name in employees:
        del employees[name]
        print(f"Працівника {name} видалено.")
    else:
        print("Працівника не знайдено.")


def find_employee():
    name = input("Введіть ПІБ для пошуку: ").strip()
    if name in employees:
        print(f"\nІнформація про {name}:")
        for key, value in employees[name].items():
            print(f"  {key}: {value}")
    else:
        print("Працівника не знайдено.")


def update_employee():
    name = input("Введіть ПІБ для зміни: ").strip()
    if name not in employees:
        print("Працівника не знайдено.")
        return

    print("Що змінити? (телефон / email / посада / кабінет / skype)")
    field = input("Поле: ").strip().lower()

    if field in employees[name]:
        new_value = input(f"Нове значення для '{field}': ").strip()
        employees[name][field] = new_value
        print("Дані оновлено.")
    else:
        print("Невірне поле.")


def show_all():
    if not employees:
        print("Список порожній.")
        return
    print("\nУсі працівники:")
    for name, data in employees.items():
        print(f"\n{name}:")
        for key, value in data.items():
            print(f"  {key}: {value}")

while True:
    print("\n--- Фірма ---")
    print("1. Додати працівника")
    print("2. Видалити працівника")
    print("3. Знайти працівника")
    print("4. Змінити дані")
    print("5. Показати всіх")
    print("0. Вихід")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        add_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        find_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        show_all()
    elif choice == "0":
        print("До побачення!")
        break
    else:
        print("Невірний вибір.")

#4
def merge_dicts(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result


d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}

merged = merge_dicts(d1, d2)
print(merged)

#5
text = input("Введіть текст: ").lower()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nКількість слів:")
for word, count in word_count.items():
    print(f"{word}: {count}")