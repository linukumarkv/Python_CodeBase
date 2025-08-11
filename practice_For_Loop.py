# for i in range(Start,  Stop,  seq(increment or decrement))
# range()  is built in function to iterate over a sequence of numbers. It generates an iterator of arithmentic
# progressions. range() generates an iterator to progress integers starting with 0 upto n-1.

fruits = ["banana", "grapes", "mangoes"]

#for i in fruits:
    #print(i)

for i in range(len(fruits)) :
    print(fruits[i])
    print(i)

for i in range(5):
    print(f"{i} ==> Linu")

for i in range(1,11):
    print(f" {i} * 2 = {i*2}")

for i in range(1,11,2):
    print(i)

for i in range(1, 20, 3):
    if i == 10:
        break
    print(i)


for i in range(1, 30, 3):

        if i == 10:
            continue
        print(i)

for i in range(1,21):
     if i==1:
         pass
     else:
        print(i)
