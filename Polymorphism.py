# poly -> many
# morph -> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def makeSound(self):
        print("Meow! Meow! Hamba! Hamba!")

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("I don't like sound!")

class Chicken(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("Kuk kuk, kruk kruk!")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def makeSound(self):
        print("Bhaaeee Bhaaeee")

billi = Cat('Billi')
sonali = Chicken('Sonali')
chagol = Goat('Chagol')

animals = [billi, sonali, chagol]

for animal in animals:
    animal.makeSound()