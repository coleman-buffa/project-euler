# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Pseudocode
# Make a list of Fibonacci sequence. Stop when the next value would be greater than 4M
  # each number is the sum of the previous two terms. Start with 1,2

fibnext = 0
fibcurrent = 1
fibprevious = 1
sum = int(0)

while fibcurrent < 4000000:
    if fibcurrent % 2 == 0:
        sum += fibcurrent
    fibnext = fibcurrent + fibprevious
    fibprevious = fibcurrent
    fibcurrent = fibnext
print(sum)
