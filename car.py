class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def car_info(self):
        return f"{self.year} {self.color} {self.make} {self.model}"
    
    def performance(self):
        if self.make == "Mercedes" and self.model == "c63":
            return "The car has a powerful V8 engine and excellent handling."
    def engine_type(self):
        if self.make == "Mercedes" and self.model == "c63":
            return "V8 engine sound"
    
# Create an object of the Car class
car1 = Car("Toyota", "Camry", 2010, "Red")
print(car1.car_info())  # Output: 2010 Red Toyota Camry
print(f"The car is {car1.performance()}")  # Output: The car is fast
print(f"The car has a {car1.engine_type()}")  # Output: The car has a V6 engine sound
car2 = Car("Mercedes", "c63", 2015, "white")
print(car2.car_info())  # Output: 2015 white Mercedes c63
print(f"The car is {car2.performance()}")  # Output: The car is 9 years old.
print(f"The car has a {car2.engine_type()}")  # Output: The car has a V8 engine sound
car3 =Car("BMW", "X5", 2018, "Black")
print(car3.car_info())  # Output: 2018 Black BMW X5