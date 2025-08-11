##List 
## identity operator 'in' returns true or false 

x=["Banana","Grapes","Mango"]
print("Banana" in x)


"""-------------------------------------------------------------------------------------------------------
Nidhi and Shubh are two students in the same grade. They have a total of 3 subjects in the school. After 
examination, they want to check whether their total marks are equal or not. So to help them write a program in 
python to take marks as input from two students. Print the overall score of both the students. Also, print "true" if 
they have an equal score or print "false" on the screen.
● Hint: Take the input for marks and then use the “==“ operator to print the answer
"""
marksNidhi = int(input("Enter the Todatl marks for Nidhi: "))
marksShubh = int(input("Enter the Todatl marks for Shubh: "))

if (marksNidhi==marksShubh):
    print("True")
else:
    print("False")

"""--------------------------------------------------------------------------------------------------------
Varun is using a stopwatch to calculate his running speed. The stopwatch shows the time taken in seconds. He
wants to convert it into minutes and seconds. Write a program to help him with this.
"""

seconds = int(input("Enter the time in seconds: "))

minutes = float(seconds//60)
sec = seconds % 60

print(f"{minutes} minutes and  {sec} seconds")

"""------------------------------------------------------------------------------------------
Varun measures his running speed in kilometers per hour. For a better understanding, he wants to
know his speed in meters per second as well. But he is facing a problem in calculating his speed in
meters per second. Write a program for Varun where he can enter the speed in kilometers per hour and
he can get the speed in meters per second.
he can get the speed in meters per second.
"""

speed_km = int(input("Enter the Speed in km/hr: "))

speed_meterPerSec = speed_km* 1000/(60*60)

print(f"{speed_meterPerSec} meter per second")


"""---------------------------------------------------------------------------------------------
Nidhi loves to travel to different countries. She is now in a country where the temperature is measured 
in Fahrenheit and she is not able to understand it in a better way. To help her in this situation, write a 
program to convert temperature from Fahrenheit to celsius.
● Hint: (0°C × 9/5) + 32 = 32°F
"""

inPutTemp = int(input("Enter the temperature in Fahrenheit: "))

 #t= (inPutTemp *9/5) + 32

temperature = (inPutTemp - 32) *5/9

print(f" The temperature is {temperature} Celsius ")


