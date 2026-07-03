hotdogVendors = open("Hotdogs.txt", "r")

print ("-----------WELCOME TO HOT DOG VENDORS-----------")
print ("Would you like to edit the file? Type Y if yes.")
editTrue = input()
if editTrue == "Y":
    openVendors = open("Hotdogs.txt", "w")
