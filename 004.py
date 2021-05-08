# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def calcPalindrome ():
    maxPal = int(0)
    for i in range (999, 500, -1):
        for j in range (999, 500, -1):
            tempProduct = i * j
            if checkPalindrome(tempProduct):
                if (maxPal < tempProduct):
                    maxPal = tempProduct
    print(maxPal)

def checkPalindrome (n):
    temp = n
    revNum = 0
    while (n>0):
        digit = n % 10
        revNum = revNum * 10 + digit
        n = n // 10
    if (temp == revNum):
        return True
    else:
        return False
        
calcPalindrome()