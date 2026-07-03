def binarySearch(searchArray, target):
    left = 0
    right = len(searchArray) - 1
    while left <= right:
        middle = (left + right) // 2
        if searchArray[middle] == target:
            return true
        elif searchArray[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return false
