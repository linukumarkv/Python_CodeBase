choice = int(input("Enter the first number: "))

if (choice%2==0):
    if 2<=choice<=5: ## Also num>=2 and num<=5
       print("Not Weird")
    elif 6<=choice<=20: 
       print("Weird")
    elif choice>20:
       print("Not Weird")

else:
   print("Weird")


"""else:
match choice:
    case 2:
    print("Not Weird")
    """

"""--------------------------------------------------------------------------------------------------
Shubham is worried about his health. He keeps checking his height and weight daily. Recently he came to 
know about the BMI report, and now he wants to calculate his own BMI by writing a python program. Write 
a program in python to check your BMI by putting your height and weight as input.
Note: Body Mass Index is a simple calculation using a person's height and weight.
The formula is BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in meters 
squared. A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. BMI applies to most
adults 18-65 years.
"""

height = float(input("Enter the height :"))
weight = float(input("Enter the Weight :"))

bmi = float(weight/(height*height))
print(bmi)

if bmi>= 25:
    print("Overweight")
elif 18.5 <= bmi <=24.9:
    print("Healthy")


    """---------------------------------------------------------------------------------------------------
A year consists of 365 days. But once in every four years, it consists of 366 days. And that is known as a
leap year. Shisha wants to know whether the current year is a leap year or not. She found that any year 
divisible by 4 is a leap year, if the year is divisible by 100 then it will not be a leap year, and if the 
year is divisible by 400 then it will be a leap year. Write a program in python to check whether the given
year is a leap year or not to help Shisha  Hint: Use if elif else condition
"""

year = int(input("Enter the year: "))

if ((year % 4==0) or (year % 400 ==0)):
   print("Leap Year")
elif (year % 100 ==0):
   print("Not a Leap Year")
else:
   print("Not a Leap Year")