# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

#Pseudocode 
# Iterate through all the numbers up N and check if it is a multiple of 3 or 5.
# If it is add it to a running sum. Otherwise do nothing. Return or print the sum

sum = int(0)
for i in range (1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)



