def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid  = low + (high - low) // 2 #to avoid overflow
    
    while low <= high:
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
        
arr = [1, 2, 3, 4, 5, 6]
x = 3

result = binary_search(arr, x)
if result != -1:
    print("target at found at index " + str(result))
else:
    print("target not in the list")