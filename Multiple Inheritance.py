class School:
    def __init__(self, name, id, level) -> None:
        self.name = name
        self.id = id
        self.level = level

    def __repr__(self) -> str:
        return f'School name: {self.name}, Id: {self.id}, Class: {self.level},'

class Home:
    def __init__(self, address) -> None:
        self.address = address

    def __repr__(self) -> str:
        return f' Address: {self.address}'

class Student(School, Home):
    def __init__(self, name, id, level, address) -> None:
        School.__init__(self, name, id , level)
        Home.__init__(self, address)

    def __repr__(self) -> str:
        return School.__repr__(self) + Home.__repr__(self)

Eusha = Student('Gazipur Govt. School', 1058, 12, 'Chourasta, Gazipur.')
print(Eusha)