class Dog:
    name = None
    id = None

    # Constructor ?
    # Use to initialize the values
    # of the instance variables (Attributes)


    def sleep(self):
        print("Sleeping")


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)





#
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def start_engine(self):
#         print("Engine Started")
#
#     def drive(self):
#         print(f"Driving the {self.color} {self.brand} car.")
#
# my_car= Car("Toyota", "Blue")
# my_car.start_engine()
# my_car.drive()

