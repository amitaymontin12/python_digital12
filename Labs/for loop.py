###For loops


# list_idan=["banana","apple,mango"]
# for x in range(len(list_idan)):
#     print(list_idan[x])

# for x in range(1,11,2):
#     print(x)
#     print("wow\n")

from time import sleep
print("Now we will get all the details about your class: \n------------------------------------------------\n")
for i in range(4):
  Name=input("Enter a name: ")
  Age=int(input("Enter a age: "))
  Phone=input("Enter a phone: ")

  print("Printing student number " + str(i+1) + " Details...\n")
  sleep(3)
  print("Full name: " + Name + "\nAge: " + str(Age) + "\nPhone: " + Phone + "\n-----------------\n")

print("\nBye Bye")
