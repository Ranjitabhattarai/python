class car:
    def __init__(self, brand, battery_size):
        self.brand = brand
        self.battery_size = battery_size

# p1 = person("ranjita",20)
# print(p1.name)
# print(p1.age)
#print(p1)         this print person memory data 

my_car = car("toyota", "100")
print(my_car.brand)
print(my_car.battery_size)

class fullname:
    def __init__(self, name, cast):
        self.name = name
        self.cast = cast

my_name = fullname("ranjita", "bhattarai")
print(my_name.name, my_name.cast)


class Electriccar(car):
    def __init__(self, brand, battery_size, color):
        super().__init__(brand, battery_size)
        self.color = color


my_electric_car = Electriccar("Tesla", "200", "Red")

print(my_electric_car.brand)
print(my_electric_car.battery_size)
print(my_electric_car.color)

