from time import sleep

choise=input("Menu:\n-----\n1.Insert Number and ** by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a String is Polindrom\n")
if(choise == "1"):
    print("The new number is: " + str((int(input("Enter a number: ")))**3))
elif(choise == "2"):
    new_list=[]
    new_list.append(input("Enter new IP: "))
    new_list.append(input("Enter new IP: "))
    new_list.append(input("Enter new IP: "))
    new_list.append(input("Enter new IP: "))
    print("\nThe new list:\n------------\n"  + str(new_list))
elif(choise == "3"):
    DNS_Dictionary={}
    DNS_Dictionary.update({input("Enter a URL: " ) : input("Enter IP: ")})
    DNS_Dictionary.update({input("Enter a URL: ")  : input("Enter IP: ")})
    DNS_Dictionary.update({input("Enter a URL: ")  : input("Enter IP: ")})
    DNS_Dictionary.update({input("Enter a URL: ")  : input("Enter IP: ")})
    print("The new dics_dict:\n-----------------\n" + str(DNS_Dictionary))
elif(choise == "4"):
    word=input("Enter a word: ")
    if (word == word [::-1]):
        print("This is Polindrom!")
    else:
        print("This isn't Polindrom!")
else:
    print("Enter 1-4 only!!..")
