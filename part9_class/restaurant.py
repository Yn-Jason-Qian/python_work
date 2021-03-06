class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def restaurant_describe(self):
        print("Restaurant name is " + self.restaurant_name)
        print("Restaurant's cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name + "is opening now.")

    def set_number_served (self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can not roll back the number served.")

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        flavor_str=""
        for flavor in self.flavors:
            flavor_str+=flavor + ", "
        print("Flavors: " + flavor_str)

restaurant = Restaurant("JIXIANG", "chinese")
restaurant.restaurant_describe()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(2)
print(restaurant.number_served)

iceCream_stand = IceCreamStand("litte shop", "chinese", ["yili", "mengniu"])
iceCream_stand.show_flavors()
