def bubble_sort(arr): # repeatedly compares adjacent elements and swaps them if needed (O(n²))
    arr = arr.copy() # creates a copy of the data to avoid modifying the original data
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:# stops early if the data is already sorted
            break
    return arr

def insertion_sort(arr): # insertion sort algorithm (O(n²))
    # sorted list one element at a time
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key # insert key into correct position
    return arr

def selection_sort(arr): # selection sort algorithm (O(n²))
    # repeatedly selects the smallest element and places it in correct position
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i # assumes the current index is minimum
        for j in range(i + 1, n): # finds actual minimum in remaining list
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # swaps with the min value found
    return arr

def quick_sort(arr): # quick sort algorithm (O(n log n))
    # uses divide and conquer approach
    arr = arr.copy()
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    # splits into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) # sorts and combines

def merge_sort(arr): # merge sort algorithm (O(n log n))
    # splits and merges lists
    arr = arr.copy()
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2 # splits list into halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right) # merge the sorted halves

def merge(left, right): # helper function for merge sort
    merged = []
    i = j = 0
    while i < len(left) and j < len(right): # merges elements in sorted order
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # adds the remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged