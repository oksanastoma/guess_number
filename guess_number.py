import random
# from colorama import init
from colorama import Fore, Back, Style
# init()
N = random.randint(0, 100)
counter = 0
print("vvedi chislo 0 - 100")
# value = int(input())

value = int(N/2)

while value != N:
    value = int(input())
    if value > N:
        print(Fore.BLUE + "mnogo" + Fore.RESET + Back.RESET + Style.RESET_ALL) # blue color
        # print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    if value < N:
        print(Fore.RED + "malo" + Fore.RESET + Back.RESET + Style.RESET_ALL)  # red color
        # print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    counter = counter + 1

print(counter) 