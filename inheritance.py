#inhertance a child class inherits from a parent class and can access its attributes and methods. The child class can also have its own attributes and methods, and it can override the methods of the parent class if needed.
#super/parent class
class Animal:
    def __init__(self, name, species, age, breed):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed

    def speaks(self):
        return "hello"
    def supermethod(self):
        return "This is a method from the parent class."
#child class
class Dog(Animal):
    def speaks(self):
        return "Woof!"
    def chrome(self):
        return "hello from a method in dog class."
    #add a class cat can inherite from animal
    #add speaks method to cat class that returns "Meow!"
# Create an object of the Dog class
mydog = Dog("Buddy", "Golden Retriever", 3, "Golden Retriever")
print(mydog.name)  # Output: Buddy  
#call a parent method
print(mydog.supermethod())  # Output: This is a method from the parent class.
#overriding method
print(mydog.speaks())  # Output: Woof!
#calling our own method
print(mydog.chrome()) 
#Creating cat object
class Cat(Animal):
    def speaks(self):
        return "Meow!"
mycat = Cat("Whiskers", "Maine Coon", 2, "Maine Coon")
print(mycat.name)  # Output: Whiskers
print(mycat.speaks())  # Output: Meow!
