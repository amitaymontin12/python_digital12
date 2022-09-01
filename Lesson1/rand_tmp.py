from random import randint
from time import sleep
print("Getting random numbers...\n")
sleep(3)

num1=randint(1,37)
num2=randint(1,37)
print("1st Number: " + str(num1) + "\n2nd Number: " + str(num2) + "\n")
if (num1==num2):
    print("You won 100$\n")
else:
    print("You won 0$\n")
print("Bye, bye")
