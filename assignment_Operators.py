a, b = 12, "Python"
## unpacking
print(a) ##12
print(b)  ##Python

"""--------------------------------------------------------------------------------------------
Anu wants to fence the garden in front of her house, on three sides with lengths 20 m, 12 m, and 12 m.
Find the cost of fencing at the rate of ` 150 per meter 
Hint: Find the perimeter and then calculate the total cost of fencing

"""
perimeter = 20+12+12
cost = perimeter * 150
print("The cost for Fencing is :",cost)

"""---------------------------------------------------------------------------------------------
4)	A farmer dug a flower bed of radius 7 m at the center of a field. He needs to purchase fertilizer.
 If 1 kg of fertilizer is required for 1 square meter area, how much fertilizer should he purchase? 
 Write a python program to find the answer.
"""
area = 3.14 * 7 * 7
quantity = area*1

print(f" The farmer needs to purchase  {quantity} kg of fertilizer")