from abc import ABC, abstractmethod
# abstract base class

class Animal(ABC):
    @abstractmethod # -> enforce all derived class to have a method call eat

    def eat(self):
        print('I need bushi not bhuski!')

    @abstractmethod # -> enforce all derived class to have a method call move
    def move(self):
        pass

class Goat(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()

    def eat(self):
        print('Khaja baba Khaja baba!')

    def move(self):
        print('Move the chair chagol!')

Chagol = Goat('Chagol')
Chagol.eat()