#list=used to mutple element in a simple variable
#list is ordered,changeable and allows duplicate 
from operator import index


students=["Shelby","John","Jane","Doe"]
mynums=[1,2,3,4,5]
print(students)
print(mynums)
print(type(students))
print(type(mynums))
#len()-length
print(len(students))
print(len(mynums))
#accessing list items
print(students[0])
print(students[3])
#modifying list items
print(students)
students[1]="Smith"
print(students)
#list methods ,append(),insert(),remove(),pop(),clear()
#append()-adds an item to the end of the list
students.append("Alice")
print(students)
#remove-removes a specific item
students.remove("Jane")
print(students)
#insert()-adds an element at a specific index
students.insert(1,"Bob")
print(students)
#looping through a list
for x in students:
    print(x)
#list of courses
courses=["Math","Science","History","English"]
#
