from time import sleep

print("Now we will get all the details about your class: \n------------------------------------------------\n")
for i in range(4):
    name=input("Enter a name: ")
    age=int(input("Enter an age:"))
    phone=input("Enter a phone:")
    print("Printing student nummber " + str(i+1) + " Details...\n")
    sleep(3)
    print("Full name: " + name + "\nAge: " + str(age) + "\nPhone: " + phone + "\n-----------------\n")

print("Bye Bye")