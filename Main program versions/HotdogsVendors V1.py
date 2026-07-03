hotdogVendors = []
#Creates a new list called hotdogVendors to save the contents of the CSV file into

file = open("Hotdogs.txt", "r")
#Opens the Hotdogs.txt CSV file

for line in file:
    row = line.strip().split(",")
    hotdogVendors.append(row)
    print(row)
#Saves each vendor in their own 'row' in the array with their data in the respective 'column'
    
file.close()
#Closes the Hotdogs.txt CSV file



#This is my user interface (first version)
print ("---------------WELCOME TO HOT DOG VENDORS---------------")
while exitInterface == False:
    print ("Would you like to:\n1. Print all of the vendors",
           "\n2. Search for a certain vendor by vendor name",
           "\n3. Search for a vendor by vendor ID",
           "\n4. Sort the list (Name of vendors A-Z)",
           "\n5. Exit the program")

    
#####################################
#            Timestamp              #
#    V1 created 11/03/26 @ 13:48    #
#####################################

