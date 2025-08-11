
#print("The language is ; \nPython")
#print("Choose the following options ; \n1.Add \n2.Subract \n3.Multiply")

"""--------------------------------------------------------------------------------------------------
 1.	Your school principal wants to print the number of years left for
 retirement of the staff by collecting their  name and age. But he has no idea on how to do that.
 Help him to create a python program that gets the staff name and age and print the following statement
 as output - print(name, “ has “,years,” for retiring”). [HINT: Consider the retirement age as 50]
"""

name = input("Enter the name: ")
age = int(input("Enter the age: "))

yearsToRetire = 50-age
if  age<=50:
    print(f"{name} has {yearsToRetire} more years for retiring")
else:
    print("Retired")

"""----------------------------------------------------------------------------------------------------
2.	It's D-marts 10th Anniversary and is planning for a big give away and in order to choose the lucky 
draw winner D-mart first needs to collect all of its customer details such as name, phone number, 
email id and location. On collecting the customer details D-mart even wants to thank each and ever
y customer for visiting as soon as they entered their details. Help the D-mart manager with creating this 
program.
"""

name = input("Enter the name: ")
phone = int(input("Enter the phone neumber: "))
email= input("Enter the email: ")
location = input("Enter the location: ")

print("Thanks for sharing the details")

"""---------------------------------------------------------------------------------------------------   
3.	Write a python program to get the user’s name, age and address from the user and print them in 
separate line."""
name = input("Enter the name: ")
phone = int(input("Enter the phone neumber: "))
email= input("Enter the email: ")
location = input("Enter the location: ")

print(f"{name}\n{email}\n{location}")

"""----------------------------------------------------------------------------------------------------
4. Write a program to get 2 numbers from user and store them in variables and print them as “Values
 before swapping” . After that, swap the values in those variables and print the values as “Values after
 swapping”.
"""

a = int(input("Enter the first number"))
b = int(input("Enter the Second number"))

print("First number : " ,a)
print("Second number: " ,b)

c=a
a=b
b=c

print("First number swapped to  : " ,a)
print("Second number swapped to : " ,b)

"""------------------------------------------------------------------------------------------------------
Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to 
know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write 
a program in python to check your BMI by putting your height and weight as input.
Note: Body Mass Index is a simple calculation using a person's height and weight.
The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters 
squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most
adults 18-65 years.
"""

height = int(input("Enter the height :"))
Weight = int(input("Enter the Weight :"))

bmi = float(weight/height)
if bmi>= 25:
    print("Overweight")
elif 18.5 >= bmi <=24.9:
    print("Healthy")