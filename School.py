class Student:
    def __init__(self, name, id, stdClass):
        self.name = name
        self.id = id
        self.stdClass = stdClass

    def __repr__(self) -> str:
        return f'Student name: {self.name}, Id: {self.id}, Class: {self.stdClass}'
    
class Teacher:
    def __init__(self, name, id, subject):
        self.name = name
        self.id = id
        self.subject = subject
    
    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, Id: {self.id}, Subject: {self.subject}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def addTeacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, id, subject)
        self.teachers.append(teacher)

    def enrollStudent(self, name, fee, stdClass):
        if fee < 6500:
            return f'{name} does not have enough money to enroll:)'
        else:
            id = len(self.students) + 1001
            student = Student(name, id, stdClass)
            self.students.append(student)
            return f'Student name: {student.name} enrolled successfully with id: {student.id} in class: {student.stdClass}'
        
    def __repr__(self) -> str:
        print('Welcome to ',self.name)
        print('Our Teachers: ')
        for teacher in self.teachers:
            print(teacher)

        print('Our Students: ')
        for student in self.students:
            print(student)

        return f'Thank You!'

# std1 = Student('Sabit', 102, 9)
# print(std1)

# teacher1 = Teacher('Hannan', 99, 'Data Structure')
# print(teacher1)

diu = School('Daffodil')
diu.enrollStudent('Jubu', 6900, 12)
diu.enrollStudent('Shuvo', 6200, 12)

diu.addTeacher('Sumit', 'Javascript')
diu.addTeacher('Samia Sayed', 'OS')

print(diu)
