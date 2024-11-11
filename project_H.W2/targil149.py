
def positive(num):
    sum=0
    for i in range(1,num):
        sum=sum+(i**3)
    print("The summary is: " + str(sum))
    return sum



##main code##
new_sum=positive(int(input("Enter a positive number: ")))