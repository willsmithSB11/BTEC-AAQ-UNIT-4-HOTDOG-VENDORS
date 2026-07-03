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

#Binary search algorithm
def binarySearch(searchArray, target):
    left = 0
    right = len(searchArray) - 1
    while left <= right:
        middle = (left + right) // 2
        if searchArray[middle] == target:
            print("Item found in index: ", middle)
            return middle
            return True
        elif searchArray[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

#Bubble sort algorithm
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Quick sort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [ x for x in arr if x > pivot]
    combined = quicksort(less) + equal + quicksort(greater)
    print ("Sorted sub-array is currently: ", combined)
    return combined

#Prints the list in rows
def listInRows(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])

        
#Searches the array using Linear search
def linearSearch(arr, target):
    for i in len(arr):
        for x in len(arr[i]):
            if len[i][x] == target:
                print ("Item found in index: ", x,"\nOn line: ", i)
                print ("Vendor Info: ", i)
                return True

#Sets a boolean value to allow the user to use the interface until they choose to exit
exitInterface = False
#Stores the sorted status of the array as a boolean value
arraySorted = False
#Adds a title to the array in index 0
title = "VENDOR ID","VENDOR NAME","YEAR & WEEK","VEGAN","MEAT","ONIONS(KG)","KETCHUP(L)"
hotdogVendors.insert(0,title)
#Validates the vendor ID
vendorIDCorrect = False
for i in range(len(hotdogVendors)):
    vendorID = hotdogVendors[i][0]
    
    if (len(vendorID))==6 and vendorID[:2].isalpha() and vendorID[2]=="_" and vendorID[3:].isdigit():
        vendorIDCorrect = True
        print("Vendor ID for", hotdogVendors[i],"is formatted correctly")
#This is my user interface (first version)
print (">--------------WELCOME TO HOT DOG VENDORS--------------<")
while exitInterface == False:
    print ("Would you like to:\n1. Print all of the vendors",
           "\n2. Search for a certain vendor by vendor name",
           "\n3. Search for a vendor by vendor ID",
           "\n4. Sort the list (Name of vendors A-Z)",
           "\n5. Exit the program")
    userOption = int(input())
    match userOption:
        case 1:
            for i in range(len(hotdogVendors)):
                print (hotdogVendors[i])

        case 2:
            #Asks the user which searching algorithm they want to use
            print ("What vendor name are you looking for? (Ensure your input is formatted in proper english)")
            vendorNameSearch = input()
            print ("Would you like to use:\n1. Binary Search\n2. Linear search")
            algorithmUse = int(input())
            #Checks if the list is sorted using the boolean value from earlier
            #Asks the user if they would like to sort the l
            if algorithmUse == 1:
                if arraySorted != True:
                    #informs the user if the 
                    print("To use binary search, the array must be sorted. Would you like to sort it now? (Y/N)")
                    sortNow = input()
                    if sortNow == "Y":
                        whichSort = input("Which sort would you like to use:\n1. Bubble Sort\n2. Quick Sort")
                        if whichSort == 1:
                            print("Sorted algorithm:")
                            bubbleVendors = bubbleSort(hotdogVendors)
                            print(bubbleVendors)
                        elif whichSort == 2:
                            print("Sorted algorithm:")
                            quickVendors = quickSort(hotdogVendors)
                            print(quickVendors)
                    elif sortNow == "N":
                        print ("Would you like to use linear search instead? (Y/N)")
                        searchLinear = input()
                        if searchLinear == "Y":
                            linear = linearSearch(hotdogVendors, vendorNameSearch)
                            if linear == True:
                                print("yah")
                            else:
                                print("nah")
                        else:
                            print("nah")
                elif algorithmUse == 2:
                    linear = linearSearch(hotdogVendors, vendorNameSearch)

#####################################
#            Timestamp              #
#    V2 created 13/03/26 @ 09:29    #
#####################################
