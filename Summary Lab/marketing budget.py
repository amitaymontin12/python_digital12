from time import sleep
#######################
print("\n---------------------------\nWelcome To Marketing Budget\n---------------------------\nNow we will show you the marketing budget:\n1.Facebook campaign = 100ILS per day.\n2.Instagram campaign = 50ILS per day.\n")
Budget=int(input("What's your Budget: "))
Facebook=int(input("Enter How long you wants the Facebook campaign will run? "))
Instagram=int(input("Enter How long you wants the Instagram campaign will run? "))
sleep(2)
print("\nsummary of your Marketing Budget:\n---------------------------------\nFacebook: " + str(Facebook) + "\nInstagram: " + str(Instagram))
summary=((Facebook * 100) + (Instagram * 50)) * 1.17
print("\nThe summary of the cost: " + str(summary) +  " ILS with tax")
if Budget - summary > 0:
    print("Succcessful!")
    print("\nYou'll have: " + str(Budget-summary) + " ILS left")
else:
    print("You'll need to hׂad: " + str((Budget - summary)*-1))