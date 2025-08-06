
##- Int - integer value also called as class 'int'
age = 27
print(type(age))

#<class 'float'>
p= 3.14
print(type(p))

#complex number - <class 'complex'>
c= 7j
print(type(c))

#String -  can be inside double or single quotes
#<class 'str'>

name ="Linu Kumar"  
print(type(name))

#List - to store one or more values of same or different types.
#<class 'list'>

myList = [40,"Linu", 12, 14.2]
print(myList)

print(type(myList))

# positioning  - indext positions in List
#[40, "Linu", 12, 14.2] ==>  
#[ 0     1     2    3 ]

#how to access values from positions
myList[2] # get the value in the index position 2
print(myList[2])

#How to change the values in the index position. List is MUTABLE or Changable
myList[2] = 55
print(myList[2])

#Tuple  use curly brackets instead of square brackets as in list
# Same as list but its not mutable or changeable, ordered
myTuple = (40,"Linu", 12, 14.2)
#          0     1     2    3 ]
print(myTuple)

print(type(myTuple))

#myTuple[2] = 4
print(myTuple[2])

# Set - {}  ==> prints in different order, avoid duplicates...unordered.
print("Set")

s= {30, "linu", 23.3, 55,67.2, 30}  
print(s)

##Dictionary  {} - Stored as key Value pairs.  Keys can be char or number, but ust be unique
student ={'name': "Linu", 'age': 23, 'Hobbies' : ["Coding", "cycling", 4]}
print(student['name'])
print(student['Hobbies'])
print(student['Hobbies'][1]) # To prnt "cycling" - specify the position

student['age'] = 30
print(student)

##Boolean  - True or Fasle - Keyword, first letter is capital.