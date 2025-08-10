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
