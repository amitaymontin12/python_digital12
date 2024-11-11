
#####################
from time import sleep
######################
#prices:
cola=10
sprite=7
water=5
soda=6
######################
print(" -- Welcome to Drinks Machine ---")
money = int(input("please Enter how money you have: "))

drink = input("\n-----------\n   "
                       "Menu\n-----------\nDrinks:\n1.Coca cola = 10 ILS\n2.Sprite = 7 ILS\n3.Cold Water = 5 ILS\n4.Soda = 6 ILS\n5.Exit\n")
if (drink == "1"):
    if money >= cola:
        print("\nYou selected cola")
        money = money - cola
        print("Your change is: "  + str(money) + str(" ILS"))
        sleep(1)
        print("\nGood bye")
    else:
        print("\nYou need more money")
        money = cola - money
        print(str(money) + str(" ILS"))

elif(drink == "2"):
    if money>=sprite:
        print("\nYou selected sprite")
        money = money-sprite
        print("Your change is: " + str(money) + str(" ILS"))
        sleep(1)
        print("\nGood bye")
    else:
        print("You need more money")
        money=sprite-money
        print(str(money) + str(" ILS"))

elif(drink=="3"):
    if money>=water:
        print("\nYou selected cold water")
        money=money-water
        print("Your change is: " + str(money) + str(" ILS"))
        sleep(1)
        print("\nGood bye")
    else:
        print("You need more money")
        money=water-money
        print(str(money) + str(" ILS"))

elif(drink=="4"):
    if money>=soda:
        print("\nYou selected soda")
        money=money-soda
        print("Your change is: " + str(money) + str(" ILS"))
        sleep(1)
        print("\nGood bye")
    else:
        print("You need more money")
        money=soda-money
        print(str(money) + str(" ILS"))

elif(drink=="5"):
    print("\nPlease come back soon!\n")
else:
    print("Please choose 1-4 only!")