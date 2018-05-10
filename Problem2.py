sum = 0
x = 0
y = 1

while y < 4000000:
    if y % 2 == 0:
        sum += y

    x, y = y, x + y

print(sum)