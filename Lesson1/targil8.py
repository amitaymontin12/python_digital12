from time import sleep

while(True):
    choise=input("Menu:\n-----\n1.Insert Number and ** by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a String is Polindrom\n")
    if(choise=="1"):
        print("The new number is: " + str((int(input("Enter a number: ")))**3))
    elif(choise=="2"):
        list_ip=[]
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        list_ip.append(input("Enter new IP: "))
        print("\nThe new list:\n------------\n"  + str(list_ip))
    elif(choise=="3"):
        dns_dict={}
        dns_dict.update({input("Enter a URL: " ) : input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: ")  : input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: ")  : input("Enter IP: ")})
        dns_dict.update({input("Enter a URL: ")  : input("Enter IP: ")})
        print("The new dics_dict:\n-----------------\n" + str(dns_dict))
    elif(choise=="4"):
        word=input("Enter  a word: ")
        if (word == word [::-1]):
            print("This is Polindrom!")
        else:
            print("This isn't Polindrom!")
    else:
        print("Enter 1-4 only!!...\n")

    exit=input("Do you want to exit? y/n\n")
    if(exit=="yes" or exit=="y"):
        break
    else:
        print("Welcome Back!\n")


print("\nThank you and bye bye")