dict_names={"idan":1000,"ben":2000,"dudu":3000,"dan":4000,"yona":5000}
print(dict_names)
summary=dict_names["idan"]+dict_names["yona"]
print("The summary is: " +  str(summary))
dict_names["amitay"]=summary
print(dict_names)
print("Numbers of Entries: " + str(len(dict_names)))
print("idan" in dict_names)
