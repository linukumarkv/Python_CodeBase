#whenever multiple conditions are to be checked.
age = int(input("Enter age: "))

#logical operator - and , or , not
#- and operator needs both condition to be true, or - either one should be true
# not: Returns opposite boolean value

if (age >=18) and (age<=70):
    print(age, "is Eligible")
else:
    print(age, "is Not Eligible")

##Identity Operators
#---------------------
# is - returns true if both variable are same object in memory, is not - returns true if both variables are 
# are not the same object

x= 78
y= 78

print(x==y)

#Membershipp operators
#---------------------
# in - returns true if found in a sequence
# not in - returns ture if not found in sequenc