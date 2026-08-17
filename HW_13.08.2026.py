#1
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def show_info(self):
        return f"Title: {self.title} | Author: {self.author} | Pages: {self.pages} | Current page: {self.current_page}"

    def read_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"Перейшли на сторінку {self.current_page}")
        else:
            print("Ви на останній сторінці")

    def read_pages(self, count):
        if count <= 0:
            print("Кількість сторінок має бути більше 0")
            return

        if self.current_page + count > self.pages:
            self.current_page = self.pages
            print(f"Ви на останній сторінці ({self.pages})")
        else:
            self.current_page += count
            print(f"Перейшли на сторінку {self.current_page}")

    def restart(self):
        self.current_page = 1
        print("Повернулись на першу сторінку")

    def progress(self):
        percent = (self.current_page / self.pages) * 100
        print(f"Прочитано: {percent:.1f}%")


book1 = Book("ВОНО", "Стівен Кінг", 1344)
book2 = Book("Гаррі Поттер", "Джоан Ролінг", 620)

print("Книга 1")
print(book1.show_info())
book1.read_page()
book1.read_pages(980)
book1.progress()
book1.restart()
print(book1.show_info())

print("\nКнига 2")
print(book2.show_info())
book2.read_pages(625)
book2.progress()
book2.read_page()
print(book2.show_info())

#2
class City:

    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def show_info(self):
        return f"Місто: {self.name} | Регіон: {self.region} | Країна: {self.country} | Населення: {self.population} | Індекс: {self.postal_code} | Код: {self.phone_code}"

    def change_population(self, new_population):
        self.population = new_population
        print(f"Населення міста {self.name} змінено на {self.population}")

    def change_postal_code(self, new_code):
        self.postal_code = new_code
        print(f"Поштовий індекс змінено на {self.postal_code}")


city1 = City("Львів", "Львівська область", "Україна", 720000, "79000", "032")
city2 = City("Одеса", "Одеська область", "Україна", 1010000, "65000", "048")

print("Місто 1")
print(city1.show_info())
city1.change_population(735000)
city1.change_postal_code("79001")
print(city1.show_info())

print("\nМісто 2")
print(city2.show_info())
city2.change_population(1025000)
print(city2.show_info())

#3
class Country:

    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def show_info(self):
        cities_str = ", ".join(self.cities)
        return f"Країна: {self.name} | Континент: {self.continent} | Населення: {self.population} | Код: {self.phone_code} | Столиця: {self.capital} | Міста: {cities_str}"

    def add_city(self, city_name):
        if city_name not in self.cities:
            self.cities.append(city_name)
            print(f"Місто «{city_name}» додано")
        else:
            print(f"Місто «{city_name}» вже є у списку")

    def remove_city(self, city_name):
        if city_name in self.cities:
            self.cities.remove(city_name)
            print(f"Місто «{city_name}» видалено")
        else:
            print(f"Місто «{city_name}» не знайдено")

    def change_population(self, new_population):
        self.population = new_population
        print(f"Населення країни {self.name} змінено на {self.population}")


country1 = Country("Україна", "Європа", 41000000, "+380", "Київ", ["Київ", "Львів", "Одеса", "Харків"])
country2 = Country("Польща", "Європа", 38000000, "+48", "Варшава", ["Варшава", "Краків", "Гданськ"])

print("Країна 1")
print(country1.show_info())
country1.add_city("Дніпро")
country1.remove_city("Харків")
country1.change_population(40500000)
print(country1.show_info())

print("\nКраїна 2")
print(country2.show_info())
country2.add_city("Вроцлав")
country2.change_population(37500000)
print(country2.show_info())