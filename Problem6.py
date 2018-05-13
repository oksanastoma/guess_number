# Find the difference between the sum of the squares 
# of the first one hundred natural numbers and the square of the sum.

import math

s1 = 0 #sum of the squares
sum = 0
s2 = 0 #the square of the sum

for i in range(1, 101):
    s1 += i*i
    sum += i
s2 = sum**2
print ("The difference: " + str(abs(s1 - s2)))