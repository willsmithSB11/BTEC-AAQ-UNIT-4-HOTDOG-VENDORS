from array import array
#Replace arr with array name
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


### EXAMPLE ARRAY AND SORT ###

array[34,7,53,26,18,42,56,123,90]
print("Original array", array)
bubble_sort(array)
print ("Sorted array:", array)
