##Dictionary  {} - Stored as key Value pairs.  Keys can be char or number, but ust be unique
student ={'name': "Linu", 'age': 23, 'Hobbies' : ["Coding", "cycling", 4]}
print(student['name'])
print(student['Hobbies'])
print(student['Hobbies'][1]) # To prnt "cycling" - specify the position

student['age'] = 30
print(student)

##Boolean  - True or Fasle - Keyword, first letter is capital.

## checking number values in dictionary
number= {1:"One", 2:"Two", 3:"Three", 4:"Four" }
num = int(input("Enter the Number 1- 4: "))
if num in number:
    print(number[num])
else:
    print("Not valid")

## checking number values in List
