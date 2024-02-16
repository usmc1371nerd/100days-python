#Encapsulation 

class Car:
    def __init__ (self, make, model, year):
        self.make= make
        self.model= model
        self.year= year
        
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading =  mileage
        else:
            print("You can't roll back and odemeter")


my_car = Car("Ford",  "F-150",  1992)
print(my_car.get_description())


#Inheritiance 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal Sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
    
# dog = Dog("Peebles")

# print(dog.name + " says: " + dog.speak())
