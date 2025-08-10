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