# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

z = 20
x = False
while x == False: 
    if z % 11 == 0 and z % 12 == 0 and z % 13 == 0 and z % 14 == 0 and z % 15 == 0 and z % 16 == 0 and z % 17 == 0 and z % 18 == 0 and z % 19 == 0 and z % 20 == 0:
        x = True
        print(z)           
    z += 20