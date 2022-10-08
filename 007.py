# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def calcPrime (n):
    prime_list = [2]
    prime_candidate = int(3)
    while len(prime_list) < n:
        if checkPrime(prime_list, prime_candidate):
            prime_list.append(prime_candidate)
        prime_candidate += 2
    return prime_list[-1]

def checkPrime (list, num):
    for prime in list:
        if prime < int(math.sqrt(num)) + 1:            
            if num % prime == 0:
                return False
    return True

print (calcPrime(10001))


