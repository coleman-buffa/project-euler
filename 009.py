# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Use Euclid's formula
def pyTriple():
    for m in range(1000):
        for n in range(1000):
            if (m > n):
                b = m**2 - n**2
                a = 2 * m * n
                c = m**2 + n **2
                if ((a**2 + b**2 == c**2) and (a+b+c == 1000)):
                    print(a,b,c)
                    print(a*b*c)

pyTriple()