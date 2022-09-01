my_details=["Amitay montin",16,"amitymon128@gmail.com","0549087167"]
print("Full name: " + my_details[0] + "\nage: " + str(my_details[1]) + "\nmail: " + my_details[2] + "\nPhone: " + my_details[3])

ip_list=["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)
ip_list.pop(2)
print(ip_list)
print("IP list length is: " + str(len(ip_list)) + "\nAnd the IP List: " + str(ip_list))
