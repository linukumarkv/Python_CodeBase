age = int( input("Enter the age:  "))

is_member = True

if age >=60 :
   print("Eligible for discount")
   if is_member:
       print("Get 30% discount")
   else:
       print("Get 10% discount")
else:
    print("Not Eligible for discount")