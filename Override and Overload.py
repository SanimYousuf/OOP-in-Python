class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Eaating anda!!')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('Only protein and anda!!')

    def exercise(self):
        print('Must be a gym dude!!')

    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.age * other.age
    
    def __gt__(self,other):
        return self.age > other.age

Ben = Cricketer('Ben Cutting', 34, 6.2, 89, 'Australia')
Ben.eat()
Ben.exercise()

Warner = Cricketer('David Warner', 36, 5.6, 78, 'Australia')

print(Ben + Warner)
print(Ben * Warner)
print(Ben > Warner)