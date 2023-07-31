class Girlfriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f" Я девушка . Меня зовут {self.name}. Мне {self.age} лет.")

    def person(self):
        print("Жена")


class Boyfriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Я парень. Меня зовут {self.name}. Мне {self.age} лет.")

    def person(self):
        print("Муж")


Girlfriend_1 = Girlfriend("Наташа", 29)
Boyfriend_1 = Boyfriend("Рустам", 33)

for family in (Girlfriend_1, Boyfriend_1):
    family.person()
    family.info()
