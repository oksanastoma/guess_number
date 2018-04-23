import random


N = random.randint(0, 100)
counter = 0
print("vvedi chislo 0 - 100")
# value = int(input())

value = int(N/2)

while value != N:
    value = int(input())
    if value > N:
        print("mnogo")
    if value < N:
        print("malo") 
    counter = counter + 1

print(counter)
