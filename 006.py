# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1+2+3+...+10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# (1+2+3+ ... + 100)^2 - (1^2 + 2^2 + 3^2 + ... + 100^2) = ?

def calcSumOfSquares(n):
    sum = int(0)
    for i in range(n+1):
        sum += i ** 2
    return sum

def calcSquareOfSum(n):
    sum = int(0)
    for i in range(n+1):
        sum += i
    sum = sum ** 2
    return sum

print (calcSquareOfSum(100) - calcSumOfSquares(100))
