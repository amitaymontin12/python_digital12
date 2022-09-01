my_dict={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"]}
print("7.7.7.7" in my_dict.values())

print(my_dict)
 my_dict.update({"www.net4u.com":"33.33.33.33","www.walla.com":"66.66.66.66."})
 print(my_dict)
print("Number of Entries: " + str(len(my_dict)))
 print(my_dict["www.google.com"])
 print(my_dict.values())
 my_dict["www.google.com"]="8.8.4.4"
 print(my_dict["www.google.com"])
 print(my_dict)
