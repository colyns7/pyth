#class is a blueprint for creaing objects.
# object is an instance of a class.
# object-atribute and methods  
class Employee:
         def __init__(self, first_name,last_name, position,salary,department):
             self.first_name = first_name
             self.last_name = last_name
             self.position = position
             self.salary = salary 
             self.department = department
#returns a reable string when you print the object
         def __str__(self):
                return f"Employee(name={self.first_name} {self.last_name}, position={self.position}, salary={self.salary}, department={self.department})"
         def annual_salary(self):
                return self.salary * 12
         def fullname(self):
                return self.first_name + " " + self.last_name
         
         
#create an object 
Employee_1 = Employee("Alice", "Joy", "Manager", 75000,"HR")
print(Employee_1.fullname()) # Output: Alice Joy    
print(Employee_1.position) # Output: Manager
print(f"{Employee_1.fullname()}'s salary is {Employee_1.annual_salary()}") # Output: Alice's salary is 900000
print(Employee_1.department) # Output: HR
Employee_2 = Employee("Bob", "Jacob", "Developer", 60000,"IT")
print(Employee_2.fullname()) # Output: Bob Jacob        
print(Employee_2.position) # Output: Developer
print(f"{Employee_2.fullname()}'s salary is {Employee_2.annual_salary()}") # Output: Bob's salary is 720000
print(Employee_2.department) # Output: IT
Employee_3 = Employee("Charlie", "Smith", "Designer", 55000,"Design")
print(Employee_3.fullname()) # Output: Charlie Smith
print(Employee_3.position) # Output: Designer
print(f"{Employee_3.fullname()}'s salary is {Employee_3.annual_salary()}") # Output: Charlie's salary is 660000
print(Employee_3.department) # Output: Design
#calling the annual_salary method for each employee
print(f"{Employee_1.fullname()}'s annual salary is {Employee_1.annual_salary()}") # Output: Alice's annual salary is 900000
print(f"{Employee_2.fullname()}'s annual salary is {Employee_2.annual_salary()}") # Output: Bob's annual salary is 720000
print(f"{Employee_3.fullname()}'s annual salary is {Employee_3.annual_salary()}") # Output: Charlie's annual salary is 660000
