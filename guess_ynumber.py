#import random

#N = random.randint(0, 100)

x = 0
y = 1000
while True:
    first = (x + y)//2
    
    X = input('Number: {} ? (yes, >, <)'.format(first))
    if X.lower() == 'yes':
        print('YES!!!')
        break
    elif X =='>':
        x = first + 1
    else:
        y = first - 1