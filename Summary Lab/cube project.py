#modules
from random import randint
from time import sleep

print("\n- - - - - - - - - - - - -\nWelcome to our Cube game!\n- - - - - - - - - - - - - \nEach turn cost: 3 ILS\n")
money=int(input("Enter how many money do you have? "))
turns=(money//3)
print("You have: " + str(turns) + " turns\nYour change: " + str(money%3) + " ILS\n")

#define the variable
prize = 0
for i in range(turns):
    print("Rolling Cubes for Round Number: " + str(i+1) + "\n------------------------------")
    sleep(3)
    cube1 = randint(1,6)
    cube2 = randint(1,6)
    print("Cube1: " + str(cube1) + "\nCube2: " + str(cube2) + "\n")
    if(cube1 == cube2):
        if(cube1 == 6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(cube1 == 1):
        prize=prize + 20
    elif(cube2 == 2):
        prize=prize + 40
print("Calculating your prize...")
sleep(3)
print("Your prize: " + str(prize) + " ILS")



