from random import randint
from time import sleep

##############################
def Market():
    print("\nNow we will calculate your marketing:\nPrices:\n-------\nTomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
    tomatos=int(input("Enter how many tomatos? "))
    cucumbers=int(input("Enter how many cucumbers? "))
    colas=int(input("Enter  many colas? "))
    chickens=int(input("Enter how many chickens? "))
    print("\nSummary of your order:\n----------------------\ntomatos: " + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))
    summary=(tomatos*3)+(cucumbers*2)+(colas*5)+(chickens*20)
    print("\nYou have to pay: " + str(summary) + " NIS without tax")
    print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")

#####main code#####
for i in range(10):
    Market()