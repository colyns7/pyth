#dictionary store data in key value pairs
STUDENT = {
"name" : "Shelby",
"age" : 18,
"course" : "MIT"
}
print(STUDENT)
print(type(STUDENT))
#accessing the value 
print(STUDENT["name"])
print(STUDENT["course"])
#adding key:value
STUDENT["City"] = "Nairobi"
print(STUDENT)
#updateing a value
STUDENT["Course"] = "Data Science"
print(STUDENT)
#accessing all keys
print(STUDENT.keys())
#values
print(STUDENT.values())
#items
print(STUDENT.items())
#loop through all the key
for x in STUDENT:
    print(x)
#loop through all the values
for x in STUDENT.values():
    print(x)
    #loop through all items
for x,y in STUDENT.items():
    print(x,y)