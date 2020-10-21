class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(
            f"{self.first_name} {self.last_name} is {self.age} year old {self.gender}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


paul = User("Paul", "Shuravin", 28, "male")
john = User("John", "Doe", 32, "male")
alice = User("Alice", "Smith", 24, "female")

paul.describe_user()
paul.greet_user()

john.describe_user()
john.greet_user()

alice.describe_user()
alice.greet_user()
