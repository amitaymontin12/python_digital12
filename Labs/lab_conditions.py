'''
write a code that will show the menu:
Menu:
1.Insert Number and ** it by 3
2.Insert 4 Ips to a list and print it
3.Insert 4 Entries to DNS_Dictionary and print it
4.Check if a string is Polindrom

if the user won't choose 1-4 , you will tell him to insert 1-4 only!
'''


choice=input("-------\nM e n u\n-------\n1.Insert Number and ** it by 3\n2.Insert 4 Ips to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a string is Polindrom\n")

if(choice == "1"):
    print("The new number is: " + str(int(input("Insert a number: "))**3))
elif(choice == "2"):
    list_ip = []
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    print("\nThe new list:\n------------\n" + str(list_ip))

elif(choice == "3"):
    dns_dict = {}
    dns_dict.update({input("Enter a URL: ") : input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: ") : input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: ") : input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: ") : input("Enter IP: ")})
    print("\nThe new dictionary:\n------------------\n" + str(dns_dict))
elif(choice == "4"):
    word=input("Enter a word: ")
    if word == word[::-1]:
        print("This is palindrome")
    else:
        print("This isn't palindrome")

else:
    print("Enter 1-4 only!!...")
