
x= 78
y= 78

print(x==y)  # checks the value of the variable
print(x is y)  # checks the memory location values of the variables


#Identity operator - print memory location - if number value is same , they share same memory location
print(id(x))
print(id(y))

#list  can store more than one value

l = [34, "Linu"]
j = [34, "Linu"]

print(id(l))   ## 
print(id(j))

print(l is j)  ## id is compared...is will check id but == will check values.
print (x is y)
