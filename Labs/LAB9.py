'''
Menu:
1.Dogs Details
2.Friends List
3.N Azzeret
'''
from ran_tmp import randint
from time import sleep

def menu():
    while(True):
        choice=input("Menu:\n----\n1.Dogs Details\n2.Friends List\n3.N Azzeret\n")
        if(choice=="1"):
            Dogs()
        elif(choice=="2"):
            Friends()
        elif(choice=="3"):
            Azzeret()
        else:
            print("Enter 1-3 only!!!\n")
            continue
        exit=input("Do you want to exit? yes/no\n")
        if(exit=="yes"):
            break
        else:
            print("Welcome back!\n")
    sleep(2)
    print("Bye Bye...\n")


def Dogs():
    name=input("Enter Dog's name: ")
    age=int(input("Enter Dog's age: "))
    print("\nDog's Name: " + name + "\nDog's age: " + str(age*7) + "\n")


def Friends():
    list_friends=[]
    for i in range(5):
        list_friends.append(input("Enter a friend's name: "))
    name=(input("Enter new name: "))
    if(name in list_friends):
        print(name + " is inside the list!\n")
    else:
        print(name + " isn't inside the list!\n")


def Azzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    print(str(num) + " Azzeret is: " + str(sum) + "\n")

menu()