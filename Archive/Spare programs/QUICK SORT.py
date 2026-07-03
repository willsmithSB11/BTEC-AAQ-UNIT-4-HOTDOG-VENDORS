#Replace arr for array name
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x i arr if x == pivot]
    greater = [ x for x in arr if x > pivot]
    combined = quicksort(less) + equal + quicksort(greater)
    print ("Sorted sub-array is currently: {combined}")
    return combined


### EXAMPLE ARRAY AND SORT ###


arr = [34,7,53,26,18]
print ("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
