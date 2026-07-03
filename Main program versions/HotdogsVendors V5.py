import time
hotdogVendors = []
#Creates a new list called hotdogVendors to save the contents of the CSV file into

file = open("Hotdogs.txt", "r")
#Opens the Hotdogs.txt CSV file

for line in file:
    row = line.strip().split(",")
    hotdogVendors.append(row)
#Saves each vendor in their own 'row' in the array with their data in the respective 'column'
    
file.close()
#Closes the Hotdogs.txt CSV file


#Stores the sorted status of the array as a boolean value
arraySorted = False

#Binary search algorithm
def binarySearch(searchArray, col, target):
    left = 0
    right = len(searchArray) - 1
    while left <= right:
        middle = (left + right) // 2
        if searchArray[middle][col] == target:
            return True
        elif searchArray[middle][col] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

#Bubble sort algorithm
def bubbleSort(arr, col):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j][col] > arr[j+1][col]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Quick sort algorithm
def quickSort(arr, col):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][col]
    less = [x for x in arr if x[col] < pivot]
    equal = [x for x in arr if x[col] == pivot]
    greater = [ x for x in arr if x[col] > pivot]
    combined = quickSort(less, col) + equal + quickSort(greater, col)
    return combined

#Prints the list in rows
def listInRows(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
   
        
#Searches the array using Linear search
def linearSearch(array, target):
    for i in range(len(array)):
        for n in range(len(array[i])):
            if array[i][n] == target:
                return True
    return False

#Sets a boolean value to allow the user to use the interface until they choose to exit
exitInterface = False
#Stores the sorted status of the array as a boolean value
arraySorted = False


def validateAll():
    #Validates the vendor ID
    vendorIDCorrect = False
    for i in range(len(hotdogVendors)):
        vendorID = hotdogVendors[i][0]
    
        if (len(vendorID))==6 and vendorID[:2].isalpha() and vendorID[2]=="_" and vendorID[3:].isdigit():
            vendorIDCorrect = True
            print("Vendor ID for", hotdogVendors[i],"is formatted correctly")
        else:
            vendorIDCorrect = False
            print("Vendor ID for", hotdogVendors[i],"is not formatted correctly!")

    #validates the vendor name
    vendorNameCorrect = False
    for i in range(len(hotdogVendors)):
        vendorName = hotdogVendors[i][1]
        if 2 <= len(vendorName) <= 25:
            vendorNameCorrect = True
            print ("Vendor name for", hotdogVendors[i],"is formatted correctly")
        else:
            vendorNameCorrect = False
            print ("Vendor name for", hotdogVendors[i],"is not formated correctly!")

    #validated year and week
    yearWeekCorrect = False
    for i in range(len(hotdogVendors)):
        yearWeek = hotdogVendors[i][2]
        yearsInt = int(yearWeek[:4])
        weekInt = int(yearWeek[4:])
        if 2000 < yearsInt < 2100 and 1 < weekInt < 52:
            yearWeekCorrect = True
            print ("Year and week for", hotdogVendors[i],"are formatted correcly")
        else:
            yearWeekCorrect = False
            print ("Year and week for", hotdogVendors[i],"are not formatted correctly")

    #validates number of vegan hotdogs
    veganHotdogsCorrect = False
    for i in range(len(hotdogVendors)):
        veganHotdogs = hotdogVendors[i][3]
        veganInt = int(veganHotdogs)
        if veganInt % 10 == 0:
            veganHotdogsCorrect = True
            print ("Vegan hotdogs for", hotdogVendors[i],"are formatted correcly")
        else:
            veganHotdogsCorrect = False
            print ("Vegan hotdogs for", hotdogVendors[i],"are not formatted correctly!")

    #validates meat hotdogs
    meatHotdogsCorrect = False
    for i in range(len(hotdogVendors)):
        meatHotdogs = hotdogVendors[i][4]
        meatInt = int(meatHotdogs)
        if meatInt % 10 == 0:
            meatHotdogsCorrect = True
            print ("Meat hotdogs for", hotdogVendors[i],"are formatted correcly")
        else:
            meatHotdogsCorrect = False
            print ("Meat hotdogs for", hotdogVendors[i],"are not formatted correctly!")

    #validates KG of onions
    onionsCorrect = False
    for i in range(len(hotdogVendors)):
        onions = hotdogVendors[i][5]
        if float(onions) % 0.5 == 0 and onions.replace('.', '', 1).isdigit:
            print ("Onions for", hotdogVendors[i],"formatted correctly")
            onionsCorrect = True
        else:
            print ("Onions for", hotdogVendors[i],"are not formatted correctly!")
            onionsCorrect = False
            
    #validates litres of ketchup
    ketchupCorrect = False
    ketchup = hotdogVendors[i][6]
    ketchupFloat = float(ketchup)
    for i in range(len(hotdogVendors)):
        if 1.0 <= ketchupFloat <= 4.0:
            ketchupCorrect = True
            print("Ketchup for", hotdogVendors[i],"formatted correctly")
        else:
            print("Ketchup for", hotdogVendors[i],"is not formatted correctly!")
    return True

#Adds a title to the array in index 0
title = "VENDOR ID","VENDOR NAME","YEAR & WEEK","VEGAN","MEAT","ONIONS(KG)","KETCHUP(L)"
hotdogVendors.insert(0,title)
#Sets a boolean value to allow the user to use the interface until they choose to exit
exitInterface = False
#this is my user interface (Third version)
print (">--------------WELCOME TO HOT DOG VENDORS--------------<")
while exitInterface == False:
    print ("Would you like to: ",
           "\n1. Print all of the vendors",
           "\n2. Sort the list",
           "\n3. Search for a piece of data",
           "\n4. Check that the list is valid",
           "\n5. Exit the program")
    userOption = int(input())
    match userOption:
        case 1:
            for i in range(len(hotdogVendors)):
                print (hotdogVendors[i])

        case 2:
            #Asks the user what data they want to sort by and which sorting algorithm they want to use
            print ("What data would you like to sort by?\n1. Vendor ID",
                   "\n2. Vendor Name",
                   "\n3. Year and week",
                   "\n4. Number of Vegan hotdogs",
                   "\n5. Number of meat hotdogs",
                   "\n6. Onions",
                   "\n7. Litres of ketchup")
            valueSortBy = int(input())
            valueSortBy = valueSortBy - 1
            print ("Which sort would you like to use?\n1. Bubble sort\n2. Quick sort")
            whichSort = int(input())
            if whichSort == 1:
                hotdogVendors.pop(0)
                bubbleSorted = bubbleSort(hotdogVendors, valueSortBy)
                listInRows(hotdogVendors)
                arraySorted = True
            elif whichSort == 2:
                hotdogVendors.pop(0)
                quickSorted = quickSort(hotdogVendors, valueSortBy)
                listInRows(hotdogVendors)
                arraySorted = True
                
            
            
        case 3:
            print ("What search would you like to use?",
             "\n1. Binary search",
             "\n2. Linear search")
            whichSearch = int(input())
            if whichSearch == 1:
                #Checks if the list is sorted using the boolean value from earlier
                if arraySorted == False:
                    print ("To use Binary search, the array must be sorted.\nSort now?(Y/N)")
                    sortNow = input()
                    if sortNow == "Y":
                        print("What would you like to sort by?\n1. Vendor ID\n2. Vendor name\n3. Year and week",
                              "\n4. Number of Vegan hotdogs\n5. Number of meat hotdogs\n6. Onions",
                              "\n7. Litres of Ketchup")
                        valueSortBy = int(input())
                        valueSortBy = valueSortBy - 1
                        print("Which sort would you like to use?\n1. Bubble sort\n2. Quick sort")
                        whichSort = int(input())
                        if whichSort == 1:
                            bubbleSorted = bubbleSort(hotdogVendors, valueSortBy)
                            hotdogVendors.pop(0)
                            listInRows(hotdogVendors)
                            arraySorted = True
                        elif whichSort == 2:
                            quickSorted = quickSort(hotdogVendors, valueSortBy)
                            hotdogVendors.pop(0)
                            listInRows(hotdogVendors)
                            arraySorted = True
                elif arraySorted == True:
                    print ("What data are you searching for?\n1. Vendor ID\n2. Vendor name\n3. Year and week",
                              "\n4. Number of Vegan hotdogs\n5. Number of meat hotdogs\n6. Onions",
                              "\n7. Litres of Ketchup")
                    dataBinarySearch = int(input())
                    dataBinarySearch = dataBinarySearch - 1
                    print ("What item are you looking for?")
                    itemSearch = input()
                    binary = binarySearch(hotdogVendors, dataBinarySearch, itemSearch)
                    if binary == True:
                        print ("Item found")
                    else:
                        print ("Not found")
            elif whichSearch == 2:
                print ("What item are you looking for?")
                itemSearch = input()
                hotdogVendors.pop(0)
                linear = linearSearch(hotdogVendors, itemSearch)
                if linear == True:
                    print ("found")
                else:
                    print ("Not found")
                

        case 4:
            #Removes the title to the list
            hotdogVendors.pop(0)
            #Displays a message to say wether all values are validated or not
            validated = validateAll()
            if validated == True:
                print ("All contents of the array are formatted correctly")
            elif validated:
                print ("Some contents of the array are invalid")
            #Adds a title to the array in index 0
            title = "VENDOR ID","VENDOR NAME","YEAR & WEEK","VEGAN","MEAT","ONIONS(KG)","KETCHUP(L)"
            hotdogVendors.insert(0,title)
            
        case 5:
            print("Goodbye, Thank you for using Hotdog Vendors")
            exitInterface = True

#####################################
#            Timestamp              #
#    V5 created 14/04/26 @ 12:08    #
#####################################
