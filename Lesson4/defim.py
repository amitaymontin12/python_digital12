from random import randint

def calculating(a,b):
    c=int(input("Enter a number: "))
    sum=a*b*c
    print("The sum is: " + str(sum))

def dogs_age(a):
    print("Real Dog's age: " + str(a*7))
    return a*7

def menu():
    choice=input("Menu:\n1.Printing 1-100 numbers\n2.random 2 cubes\n")
    if(choice=="1"):
        for w in range(1,101):
            print(w)
    elif(choice=="2"):
        print("Cub 1: " + str(randint(1,6)))
        print("Cub 2: " + str(randint(1,6)))
    else:
        print("1-2 only!!!..")



