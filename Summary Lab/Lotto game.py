import numpy as np


def lotteryNumbers():
    lotteryNum = []
    for i in range(6):
        lot = np.random.randint(1,37)
        while lot in lotteryNum:
            if lot in lotteryNum:
                lot = np.random.randint(1,37)
            else:
                break
        lotteryNum.append(lot)
    return lotteryNum


def checkWinning(num, lottery):
    win = 0
    wins = [3, 4, 5, 6]
    won = [10, 100, 5000, 1000000]
    for i in num:
        if i in lottery:
            win = win + 1
    for i in range(len(wins)):
        if wins[i] == win:
            return won[i]
        else:
            return 0


print("--------------------------------------\n======> Welcome to the lottery <======"
      "\n--------------------------------------")
Budget = int(input("How many money do you have for game? "))
print("----------------------------\nEnter a number between 1-37\n----------------------------")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
num4 = int(input("Fourth number: "))
num5 = int(input("Fifth number: "))
num6 = int(input("Sixth number: "))
print("The lottery numbers you entered are: \n------------------------------------\n"
      , [num1, num2, num3, num4, num5, num6])
NumList = [num1, num2, num3, num4, num5, num6]
wining = 0

while Budget >= 3:
    Budget = Budget - 3
    wining = int(checkWinning(NumList, lotteryNumbers())) + wining
print("----------------------\nyou've won", wining, "NIS")
print("\nBye, Bye")