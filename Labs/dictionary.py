'''
Create a dictionary with 5 names & money
then sum the money of the first & last names and print it to the screen.
after , add a new name with the sum of the money you calculated before
in the end , print the number of entries and check if "idan" is inside.
'''
#The code is:

dict_names = {"dudu":"25000","avi":"30000","itay":"76000","ortal":"66000","gal":"12000"}
print(dict_names)
summary=dict_names["dudu"] + dict_names["gal"]
print("The summary is: " + str(summary))

#one method
# dict_names["yoel"] = summary
# print(dict_names)
#two method
dict_names.update({"yoel":summary})
print(dict_names)
print("Number of entries: " + str(len(dict_names)))
print("idan" in dict_names)



















##dictionary
# my_dict = {"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":"www.google2.com"}
# print("www.google2.com" in my_dict.values())




# my_dict2 = {"www.net4u.com":"33.33.33.33","www.groo.com":"88.88.88.88"}
# print(my_dict)
# print(my_dict2)
# my_dict.update(my_dict2)
# print(my_dict)
#
# print("Number of Entries: " + str(len(my_dict)))
# print(my_dict["www.google.com"])
#
# my_dict["www.google.com"]="8.8.4.4"
# print(my_dict["www.google.com"])
# print(my_dict)



