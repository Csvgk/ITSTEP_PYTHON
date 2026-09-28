#1
class Airplane:
    def __init__(self, plane_type, max_passengers, current_passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __str__(self):
        return f"{self.plane_type}: {self.current_passengers}/{self.max_passengers} пасажирів"

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.plane_type == other.plane_type
        return False

    def __add__(self, other):
        if isinstance(other, int):
            new_count = self.current_passengers + other
            if new_count > self.max_passengers:
                raise ValueError("Перевищено максимальну кількість пасажирів")
            return Airplane(self.plane_type, self.max_passengers, new_count)
        raise TypeError("error addition")

    def __sub__(self, other):
        if isinstance(other, int):
            new_count = self.current_passengers - other
            if new_count < 0:
                raise ValueError("Кількість пасажирів не може бути від'ємною")
            return Airplane(self.plane_type, self.max_passengers, new_count)
        raise TypeError("error subtraction")

    def __iadd__(self, other):
        if isinstance(other, int):
            if self.current_passengers + other > self.max_passengers:
                raise ValueError("Перевищено максимальну кількість пасажирів")
            self.current_passengers += other
            return self
        raise TypeError("error addition")

    def __isub__(self, other):
        if isinstance(other, int):
            if self.current_passengers - other < 0:
                raise ValueError("Кількість пасажирів не може бути від'ємною")
            self.current_passengers -= other
            return self
        raise TypeError("error subtraction")

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


plane1 = Airplane("Boeing 737", 180, 100)
plane2 = Airplane("Airbus A320", 150, 120)
plane3 = Airplane("Boeing 737", 180, 50)

print(plane1)
print(plane2)
print(plane1 == plane2)
print(plane1 == plane3)

plane1 += 20
print(plane1)
plane1 -= 30
print(plane1)

plane4 = plane2 + 10
print(plane4)

print(plane1 > plane2)
print(plane1 < plane2)
print(plane1 >= plane3)
print(plane1 <= plane3)

#2
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __str__(self):
        return f"Площа: {self.area} м2, Ціна: {self.price}"

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


flat1 = Flat(50, 100000)
flat2 = Flat(50, 120000)
flat3 = Flat(65, 150000)

print(flat1)
print(flat2)
print(flat1 == flat2)
print(flat1 != flat3)
print(flat1 > flat2)
print(flat1 < flat2)
print(flat2 >= flat1)
print(flat3 <= flat1)

#3
import json


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Show(self):
        print(self.__str__())

    def to_dict(self):
        data = self.__dict__.copy()
        data["type"] = self.__class__.__name__
        return data

    @staticmethod
    def Save(shapes, filename):
        data = [shape.to_dict() for shape in shapes]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def Load(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        shapes = []
        for item in data:
            shape_type = item.pop("type")
            cls = globals()[shape_type]
            shapes.append(cls(**item))
        return shapes


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def __str__(self):
        return f"Квадрат: ліва верхня точка ({self.x}, {self.y}), сторона {self.side}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямокутник: ліва верхня точка ({self.x}, {self.y}), розміри {self.width}x{self.height}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Коло: центр ({self.x}, {self.y}), радіус {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Еліпс: ліва верхня точка описаного прямокутника ({self.x}, {self.y}), розміри {self.width}x{self.height}"


shapes = [
    Square(0, 0, 10),
    Rectangle(5, 5, 20, 10),
    Circle(15, 15, 7),
    Ellipse(2, 3, 12, 6),
]

Shape.Save(shapes, "shapes.json")

loaded_shapes = Shape.Load("shapes.json")

for shape in loaded_shapes:
    shape.Show()