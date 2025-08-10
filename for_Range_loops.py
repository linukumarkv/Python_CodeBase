
## print(range(5))==>  range of 5 gives the numbers 0 1 2 3 4.

"""for num in range(5):
    print(num) 0,1,2,3,4

## print(range(3,11))==>   gives the numbers 3,4,5,...11 
print("-------------")
for num in range(3,11):
    print(num)"""

"""## print(range(5))==>  starts from 3, increment bt 2 until 11
for num in range(3,11,2):
    print(num)"""

num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{i}*{num} = {i*num}")
    

for j in range (1,21):
    print(f"{j}*{num}= {j*num}")