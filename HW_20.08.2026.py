#1
class Film:
    all_titles = []
    all_ratings = []

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        Film.all_titles.append(title)
        Film.all_ratings.append(rating)

    @classmethod
    def середній_рейтинг(cls):
        if not cls.all_ratings:
            return 0
        return sum(cls.all_ratings) / len(cls.all_ratings)

    @classmethod
    def show_all_ratings(cls):
        for title, rating in zip(cls.all_titles, cls.all_ratings):
            print(f"{title}: {rating}")

    @classmethod
    def show_all_titles(cls):
        for title in cls.all_titles:
            print(title)


film1 = Film("Матриця", 9.0)
film2 = Film("Інтерстеллар", 8.7)
film3 = Film("Початок", 8.5)

Film.show_all_titles()
Film.show_all_ratings()
print(Film.середній_рейтинг())

#2
class Brain:
    def think(self):
        print("Мозок думає")


class Heart:
    def beat(self):
        print("Серце б'ється")


class Legs:
    def walk(self):
        print("Ноги йдуть")


class Human(Brain, Heart, Legs):
    def __init__(self, name):
        self.name = name

    def live(self):
        print(f"{self.name}:")
        self.think()
        self.beat()
        self.walk()


human1 = Human("Іван")
human1.live()

#3
class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        raise NotImplementedError


class StringInstrument(Instrument):
    def play(self):
        print(f"{self.name} видає звук через вібрацію струн")


class WindInstrument(Instrument):
    def play(self):
        print(f"{self.name} видає звук через потік повітря")


class PercussionInstrument(Instrument):
    def play(self):
        print(f"{self.name} видає звук через удар")


class Guitar(StringInstrument):
    def tune(self):
        print(f"{self.name} налаштовується")


class Flute(WindInstrument):
    pass


class Drum(PercussionInstrument):
    pass


class HybridInstrument(Guitar, Flute, Drum):
    def play(self):
        StringInstrument.play(self)
        WindInstrument.play(self)
        PercussionInstrument.play(self)


guitar = Guitar("Гітара")
flute = Flute("Флейта")
drum = Drum("Барабан")

guitar.tune()
guitar.play()
flute.play()
drum.play()

hybrid = HybridInstrument("Гібридний інструмент")
hybrid.play()