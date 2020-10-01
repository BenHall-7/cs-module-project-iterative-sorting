def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    l = 0
    r = len(arr) - 1

    if arr[l] > target or arr[r] < target:
        return -1

    if arr[l] == target:
        return l
    elif arr[r] == target:
        return r

    while r - l >= 2:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid
        elif arr[mid] < target:
            l = mid
        else:
            return mid
    return -1
