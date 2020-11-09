class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")

    def info(self):
        print(f"{self.name} is {self.age} y.o. {self.breed}")


grant = Dog("Grant", 4, "sheltie")
grant.bark()
grant.info()

kurt = Dog("Kurt", 5, "Golden Retriever")
kurt.bark()
kurt.info()

syoma = Dog("Syoma", 5, "yorkshire terrier")
syoma.bark()
syoma.info()
