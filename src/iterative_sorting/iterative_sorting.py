# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
         
        # find next smallest element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # swap
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        found_err = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                found_err = True
        if not found_err:
            break

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr

    if not maximum:
        maximum = max(arr)

    bucket = []
    for _ in range(0, maximum + 1):
        bucket.append(0)
    
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        bucket[i] += 1
    
    orig_index = 0
    for i, count in enumerate(bucket):
        for _ in range(count):
            arr[orig_index] = i
            orig_index += 1
     
    return arr

# "N" is the length of the array and "M" is the maximum value

# the time complexity is O(N + M)
# because we must iterate every element in arr
# and then iterate all possible values in the bucket

# the space complexity is O(M)
# because allocating the bucket requires room for M elements
# and no other operations take space
