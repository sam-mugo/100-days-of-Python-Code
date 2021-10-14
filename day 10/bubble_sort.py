def bubble_sort(arr):
    indexing = len(arr) -1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, indexing):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
            