#if statement

#if-statement specifies a block of code to be executed if a condition is true.
#if condition:
    #block of code to be executed if the condition is true

x=20
if x < 10:
    print(f"{x} is less than 10")
    #if condition:
    #block of code to be executed if the condition is true

    #a program that checks if a user is eligible to vote
age = 12
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    #a program that asks user for age and checks if they can drive
age = int(input("Enter your age: "))
if age >= 18:
    print("You can drive.")
else:
    print("You cannot drive.")
    #aprogram that asks user for a number and checks if
    #the number is even or odd .,hintevenumber%2==0
number = int(input("Enter a number to check if even or odd "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    #a program that askes user for two numbers and print the greater number
