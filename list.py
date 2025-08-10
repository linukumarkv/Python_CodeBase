## checking number values in List

number= {1:"One", 2:"Two", 3:"Three", 4:"Four" }
num = int(input("Enter the Number 1- 4: "))
if num in number:
    print(number[num])
else:
    print("Not valid")

