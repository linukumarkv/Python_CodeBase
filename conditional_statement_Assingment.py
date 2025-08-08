age = int( input("Enter the age:  "))
membership = input("Do you have membership : (Y/N) : ")

if membership == "Y":    
   is_member = True
else:
    is_member = False

if age >=60 :
   print("Eligible for discount")
   if is_member:
       print("Get 30% discount")
   else:
       print("Get 10% discount")
else:
    print("Not Eligible for discount")