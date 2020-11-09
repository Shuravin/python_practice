class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} y.o.")


class Student(Person):
    def __init__(self, name, age, year):
        Person.__init__(self, name, age)
        self.year = year

    def student_info(self):
        print(f"{self.name} is a student({self.year})")


teacher = Person("John", 32)
teacher.info()

alex = Student("Alex", 12, 5)
alex.student_info()
