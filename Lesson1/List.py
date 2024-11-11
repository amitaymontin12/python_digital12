###Lists

# my_list=[1,2,28,6.6,"dudu cohen"]
# print("My name: " + str(my_list[2]))
#
# my_list2 = list("1234567")
# print(my_list2)
#
# my_string = ''.join(my_list2)
# print(my_string)
#
# my_list3 = my_string.split()
# print(my_list3)
#
my_string = "hello world \nhow\n are you?"

my_list3 = my_string.splitlines()
print(my_list3)


my_list=["hello" , 1, 66.6, "amitay" , 55,77.7]

print("The length is: " + str(len(my_list)))

my_str = "12347343743473043"
print("The length is: " + str(len(my_str)))

###מוסיף לסוף של הרשימה
my_list.append("wow")
my_list.append("idan")
print(my_list)
print("The new length is: " + str(len(my_list)))

##מכניס ערך לרשימה בתא כל שהוא
my_list.insert(7,2)
print(my_list)
###מוציא תא מהרשימה
my_list.pop(7)
print(my_list)

###בודק אם ערך נמצא ברשימה
my_list=["google","facebook","ebay","apple"]
print("ebay" in my_list)










