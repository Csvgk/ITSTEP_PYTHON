#1
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
t3 = (7, 8, 9, 1, 10)

set1, set2, set3 = set(t1), set(t2), set(t3)

unique1 = set1 - set2 - set3
unique2 = set2 - set1 - set3
unique3 = set3 - set1 - set2

print("Unique 1: ", unique1)
print("Unique 2: ", unique2)
print("Unique 2: ", unique3)

#2
t1 = (1, 5, 3, 8, 9)
t2 = (2, 5, 7, 8, 0)
t3 = (4, 5, 6, 8, 1)

same_pos = []
min_len = min(len(t1), len(t2), len(t3))

for i in range(min_len):
    if t1[i] == t2[i] == t3[i]:
        same_pos.append(t1[i])

print("Same position: ", same_pos)

#3
numbers = (5, 12, 7, 345, 9, 88, 100, 23, 4, 999, 56)

stats = {}

for num in numbers:
    digits = len(str(abs(num)))
    if digits in stats:
        stats[digits] += 1
    else:
        stats[digits] = 1

for digits in sorted(stats):
    count = stats[digits]
    if digits == 1:
        word = "цифра"
    elif 2 <= digits <= 4:
        word = "цифри"
    else:
        word = "цифр"

    if count == 1:
        elements_word = "елемент"
    elif 2 <= count <= 4:
        elements_word = "елементи"
    else:
        elements_word = "елементів"

    print(f"{digits} {word} — {count} {elements_word}")

#4
people = [("Ганна", 22), ("Іван", 16), ("Марія", 20), ("Петро", 25)]

adults = [name for name, age in people if age > 18]
print(" ".join(adults))

#5
products = [('Яблука', 10), ('Молоко', 5), ('Хліб', 3), ('Масло', 2)]

total = sum(quantity for name, quantity in products)
print(f"Загальна кількість товарів: {total}")

#6
books = [
    ('Майстер і Маргарита', 'Михайло Булгаков', 1967),
    ('Злочин і покарання', 'Федір Достоєвський', 1866),
    ('Війна і мир', 'Лев Толстой', 1869),
    ('1984', 'Джордж Орвелл', 1949)
]

authors = []
seen = set()

for title, author, year in books:
    if author not in seen:
        authors.append(author)
        seen.add(author)

print("Список авторів без повторень:")
for author in authors:
    print(author)