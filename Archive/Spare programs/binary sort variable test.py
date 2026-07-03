hotdogVendors = []
#Creates a new list called hotdogVendors to save the contents of the CSV file into

file = open("Hotdogs.txt", "r")
#Opens the Hotdogs.txt CSV file
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [ x for x in arr if x > pivot]
    combined = quickSort(less) + equal + quickSort(greater)
    print (combined)
    return combined

for line in file:
    row = line.strip().split(",")
    hotdogVendors.append(row)
    print(row)

def binarySearch(searchArray, target):
    left = 0
    right = len(searchArray) - 1
    while left <= right:
        middle = (left + right) // 2
        if searchArray[middle][2] == target:
            print("Item found in position: ", middle)
            print("Full vendor info: ", searchArray[middle])
            print("Would you like to edit this vendor? (Y/N)")
            edit = input()
            return edit
        elif searchArray[middle][2] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

quickSort(hotdogVendors)
searchTarget = input()
binary = binarySearch(hotdogVendors, searchTarget)
if binary is True:
    print ("yeah")
else:
    print("NAHHH")
