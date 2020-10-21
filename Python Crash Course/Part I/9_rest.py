class Restaurant:
    def __init__(self, rest_name, cuisine_type):
        self.restaurant_name = rest_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} cooks {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number


# my_rest = Restaurant("Vis a vis", "french")
# print(my_rest.restaurant_name)
# print(my_rest.cuisine_type)

# my_rest.describe_restaurant()
# my_rest.open_restaurant()

# rest = Restaurant("Dodo", "american")
# print(rest.number_served)
# rest.set_number_served(3)
# print(rest.number_served)

class FrenchRest(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, has_onion):
        self.has_onion = has_onion
        super().__init__(restaurant_name, cuisine_type)


ouch = FrenchRest("Ouch", "French", "true")
print(ouch.has_onion)
