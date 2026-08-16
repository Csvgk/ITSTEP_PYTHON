#1
with open("data.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        line = input(f"Введіть рядок {i + 1}: ")
        f.write(line + "\n")

print("Рядки успішно записано у data.txt")

#2
filename = "data.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        print(f"Файл {filename} існує.")
        lines = f.readlines()
        # Кожен другий рядок (індекси 1, 3, 5...)
        for i in range(1, len(lines), 2):
            print(lines[i].rstrip("\n"))
except FileNotFoundError:
    print(f"Файл {filename} не існує.")

#3
with open("data.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

filtered = [line for line in lines if "Python" in line]

with open("filtered.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(filtered)

print("Рядки, що містять 'Python', записано у filtered.txt")

#4
filename = input("Введіть ім'я файлу: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned = "".join(ch for ch in content if not ch.isdigit())

    with open("cleaned.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("Результат збережено у cleaned.txt")
except FileNotFoundError:
    print(f"Файл '{filename}' не знайдено.")

#5
try:
    with open("log.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()

    # Розбиваємо текст на слова (через пробіли та розділові знаки)
    words = []
    current_word = ""
    for ch in text:
        if ch.isalpha() or ch == "_":
            current_word += ch
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:  # додаємо останнє слово, якщо воно є
        words.append(current_word)

    # Підрахунок частоти слів
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Сортуємо за частотою (спадання) і беремо 10 найчастіших
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_words[:10]

    with open("word_stats.txt", "w", encoding="utf-8") as f:
        for word, count in top_10:
            f.write(f"{word}: {count}\n")

    print("10 найпоширеніших слів записано у word_stats.txt")
except FileNotFoundError:
    print("Файл log.txt не знайдено.")

#6
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

reversed_lines = lines[::-1]

with open("reversed.txt", "w", encoding="utf-8") as f:
    f.writelines(reversed_lines)

print("Рядки у зворотному порядку збережено у reversed.txt")