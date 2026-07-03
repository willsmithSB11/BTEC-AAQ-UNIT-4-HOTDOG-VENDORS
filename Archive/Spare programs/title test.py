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

def linearSearch(arr, target):
    for i in len(arr):
        for x in len(arr[i]):
            if len[i][x] == target:
                print ("Item found in index: ", x,"\nOn line: ", i)
                print ("Vendor Info: ", i)
                return True

#Prints the list in rows
def listInRows(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])

#Sets a boolean value to allow the user to use the interface until they choose to exit
exitInterface = False
#Stores the sorted status of the array as a boolean value
arraySorted = False
title = "VENDOR ID","VENDOR NAME","YEAR & WEEK","VEGAN","MEAT","ONIONS(KG)","KETCHUP(L)"
hotdogVendors.insert(0,title)
listInRows(hotdogVendors)
