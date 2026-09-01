#1
class Device:
    def __init__(self, brand, power, color):
        self.brand = brand
        self.power = power
        self.color = color
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"{self.brand} увімкнено"

    def turn_off(self):
        self.is_on = False
        return f"{self.brand} вимкнено"

    def get_info(self):
        status = "увімкнений" if self.is_on else "вимкнений"
        return f"Бренд: {self.brand} | Потужність: {self.power}Вт | Колір: {self.color} | Стан: {status}"


class CoffeeMachine(Device):
    def __init__(self, brand, power, color, water_volume):
        super().__init__(brand, power, color)
        self.water_volume = water_volume  # мл

    def make_coffee(self):
        if not self.is_on:
            return "Спочатку увімкніть кавомашину!"
        if self.water_volume < 50:
            return "Недостатньо води"
        self.water_volume -= 50
        return f"Кава готова! Залишилось води: {self.water_volume} мл"

    def get_info(self):
        return super().get_info() + f" | Об'єм води: {self.water_volume} мл"


class Blender(Device):
    def __init__(self, brand, power, color, speed_levels):
        super().__init__(brand, power, color)
        self.speed_levels = speed_levels

    def blend(self, speed):
        if not self.is_on:
            return "Спочатку увімкніть блендер!"
        if speed < 1 or speed > self.speed_levels:
            return f"Оберіть швидкість від 1 до {self.speed_levels}"
        return f"Блендер працює на швидкості {speed}"

    def get_info(self):
        return super().get_info() + f" | Кількість швидкостей: {self.speed_levels}"


class MeatGrinder(Device):
    def __init__(self, brand, power, color, attachments):
        super().__init__(brand, power, color)
        self.attachments = attachments  # кількість насадок

    def grind(self):
        if not self.is_on:
            return "Спочатку увімкніть м'ясорубку!"
        return "М'ясо перемелено"

    def get_info(self):
        return super().get_info() + f" | Кількість насадок: {self.attachments}"


# Перевірка Завдання 1
print("=" * 50)
print("Завдання 1. Пристрої")
print("=" * 50)

coffee = CoffeeMachine("Philips", 1500, "чорний", 300)
print(coffee.get_info())
print(coffee.turn_on())
print(coffee.make_coffee())
print(coffee.get_info())

print()
blender = Blender("Bosch", 800, "білий", 5)
print(blender.get_info())
print(blender.turn_on())
print(blender.blend(3))

print()
grinder = MeatGrinder("Moulinex", 1200, "сірий", 4)
print(grinder.get_info())
print(grinder.turn_on())
print(grinder.grind())

#2
class Ship:
    def __init__(self, name, displacement, max_speed):
        self.name = name
        self.displacement = displacement  # водотоннажність (тонн)
        self.max_speed = max_speed        # вузли
        self.is_moving = False

    def start_moving(self):
        self.is_moving = True
        return f"Корабель {self.name} почав рух"

    def stop(self):
        self.is_moving = False
        return f"Корабель {self.name} зупинився"

    def get_info(self):
        status = "в русі" if self.is_moving else "на стоянці"
        return (f"Назва: {self.name} | Водотоннажність: {self.displacement} т | "
                f"Макс. швидкість: {self.max_speed} вузлів | Стан: {status}")


class Frigate(Ship):
    def __init__(self, name, displacement, max_speed, missile_count):
        super().__init__(name, displacement, max_speed)
        self.missile_count = missile_count

    def launch_missile(self):
        if self.missile_count <= 0:
            return "Ракети закінчилися"
        self.missile_count -= 1
        return f"Фрегат {self.name} випустив ракету. Залишилось: {self.missile_count}"

    def get_info(self):
        return super().get_info() + f" | Ракет: {self.missile_count}"


class Destroyer(Ship):
    def __init__(self, name, displacement, max_speed, torpedo_count):
        super().__init__(name, displacement, max_speed)
        self.torpedo_count = torpedo_count

    def launch_torpedo(self):
        if self.torpedo_count <= 0:
            return "Торпеди закінчилися"
        self.torpedo_count -= 1
        return f"Есмінець {self.name} випустив торпеду. Залишилось: {self.torpedo_count}"

    def get_info(self):
        return super().get_info() + f" | Торпед: {self.torpedo_count}"


class Cruiser(Ship):
    def __init__(self, name, displacement, max_speed, gun_caliber):
        super().__init__(name, displacement, max_speed)
        self.gun_caliber = gun_caliber  # мм

    def fire(self):
        return f"Крейсер {self.name} відкрив вогонь з гармат калібру {self.gun_caliber} мм"

    def get_info(self):
        return super().get_info() + f" | Калібр гармат: {self.gun_caliber} мм"


# Перевірка Завдання 2
print("\n" + "=" * 50)
print("Завдання 2. Кораблі")
print("=" * 50)

frigate = Frigate("Гетьман Сагайдачний", 3500, 32, 16)
print(frigate.get_info())
print(frigate.start_moving())
print(frigate.launch_missile())

print()
destroyer = Destroyer("Запоріжжя", 8000, 35, 8)
print(destroyer.get_info())
print(destroyer.launch_torpedo())

print()
cruiser = Cruiser("Москва", 11000, 32, 130)
print(cruiser.get_info())
print(cruiser.fire())

#3
class Money:
    def __init__(self, whole=0, cents=0):
        self.whole = whole      # гривні / долари / євро
        self.cents = cents      # копійки / центи
        self._normalize()

    def _normalize(self):
        """Переводить копійки в цілу частину, якщо >= 100"""
        if self.cents >= 100:
            self.whole += self.cents // 100
            self.cents = self.cents % 100
        elif self.cents < 0:
            # проста обробка від’ємних копійок
            borrow = (-self.cents + 99) // 100
            self.whole -= borrow
            self.cents += borrow * 100

    def set_money(self, whole, cents):
        self.whole = whole
        self.cents = cents
        self._normalize()

    def show(self):
        return f"{self.whole}.{self.cents:02d}"

    def __str__(self):
        return self.show()


class Product(Money):
    def __init__(self, name, whole=0, cents=0):
        super().__init__(whole, cents)
        self.name = name

    def reduce_price(self, amount_whole, amount_cents=0):
        """Зменшує ціну на задану суму"""
        total_cents = self.whole * 100 + self.cents
        reduce_cents = amount_whole * 100 + amount_cents

        if reduce_cents > total_cents:
            print("Неможливо зменшити ціну нижче нуля")
            return

        total_cents -= reduce_cents
        self.whole = total_cents // 100
        self.cents = total_cents % 100

    def get_info(self):
        return f"Товар: {self.name} | Ціна: {self.show()} грн"


# Перевірка Завдання 3
print("\n" + "=" * 50)
print("Завдання 3. Гроші та товар")
print("=" * 50)

money = Money(15, 75)
print("Сума:", money)

product = Product("Кава", 89, 50)
print(product.get_info())

product.reduce_price(10, 25)   # зменшуємо на 10 грн 25 коп
print("Після знижки:", product.get_info())

product.reduce_price(100)      # спроба зменшити занадто сильно
print(product.get_info())

#4
class TemperatureConverter:
    conversions_count = 0          # лічильник усіх конвертацій

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversions_count += 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversions_count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_conversions_count():
        return TemperatureConverter.conversions_count


# Перевірка Завдання 4
print("\n" + "=" * 50)
print("Завдання 4. Конвертер температури")
print("=" * 50)

print("25°C =", TemperatureConverter.celsius_to_fahrenheit(25), "°F")
print("77°F =", TemperatureConverter.fahrenheit_to_celsius(77), "°C")
print("0°C  =", TemperatureConverter.celsius_to_fahrenheit(0), "°F")
print("Кількість конвертацій:", TemperatureConverter.get_conversions_count())

#5
class LengthConverter:
    # 1 метр = 3.28084 фути
    # 1 кілометр = 0.621371 милі
    # 1 сантиметр = 0.393701 дюйми

    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(km):
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371

    @staticmethod
    def centimeters_to_inches(cm):
        return cm * 0.393701

    @staticmethod
    def inches_to_centimeters(inches):
        return inches / 0.393701


# Перевірка Завдання 5
print("\n" + "=" * 50)
print("Завдання 5. Конвертер довжини")
print("=" * 50)

print("10 метрів     =", round(LengthConverter.meters_to_feet(10), 2), "футів")
print("50 футів      =", round(LengthConverter.feet_to_meters(50), 2), "метрів")
print("100 км        =", round(LengthConverter.kilometers_to_miles(100), 2), "миль")
print("60 миль       =", round(LengthConverter.miles_to_kilometers(60), 2), "км")
print("30 см         =", round(LengthConverter.centimeters_to_inches(30), 2), "дюймів")
print("12 дюймів     =", round(LengthConverter.inches_to_centimeters(12), 2), "см")