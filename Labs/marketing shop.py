print("<---Welcome to Supermarket menu--->\nPrices:\n------\nTomato = 3 NIS\nCucumber = 2 NIS\nCola = 5 NIS\nChicken = 20 NIS\n")

##input'ים
tomatos=int(input("Enter how many tomatos: " ))
cucumbers=int(input("Enter how many cucumbers: "))
colas=int(input("Enter how many colas: "))
chickens=int(input("Enter how many chickens: "))

print("\nSummary of your order:\n---------------------\ntomatos: " + str(tomatos) + "\ncucumbers: "  + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

summary = (tomatos*3) + (cucumbers*2) + (colas*5) + (chickens*20)
print("\nYour have to pay: " + str(summary) + " NIS without tax")
print("\nYour have to pay: " + str("%.2f" % (summary * 1.17)) + " NIS with tax")
