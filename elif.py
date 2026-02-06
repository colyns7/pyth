#elif-used to test multiple conditions

if condition1:
    block of code to be executed if condition1 is true
elif condition2:
    block of code to be executed if condition2 is true
else:
    block of code to be executed if both condition1 and condition2 are false
#program that asks user for marks then prints the grade
#80-100 A
#70-79 B
#60-69 C
#50-59 D
#0-49 F
marks = int(input("Enter your marks: "))
if marks >= 80 and marks <= 100:
    print("GRADE A")
elif marks >= 70 and marks <= 79:
    print("GRADE B")
elif marks >= 60 and marks <= 69:
    print("GRADE C")
elif marks >= 50 and marks <= 59:
    print("GRADE D")
elif marks >= 0 and marks <= 49:
    print("GRADE F")
    #a program that ask user age and print
    #18-30-young adult
#31-45-adult
#45-65-mature adult
#>65-elderly
#<18-baby
age = int(input("Enter your age: "))
if age >= 18 and age <= 30:
    print("You are a young adult.")
elif age >= 31 and age <= 45:
    print("You are an adult.")
 elif age >= 46 and age <= 65:
    print("You are a mature adult.")
elif age > 65:
    print("You are elderly.")