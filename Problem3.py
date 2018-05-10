# Largest prime factor
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


import math
print("Prime factors of 600851475143: ")
number=int(600851475143)

for i in range(2, int(math.sqrt(number)) + 1): 
    while (number % i == 0): 
        print(i)
        number //= i 

if (number != 1):
    print (number)