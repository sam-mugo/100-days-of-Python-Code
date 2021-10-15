def bubble_sort(arr):    
    #len(arr) -1 the last item cant compare to any other so its the max
    indexing = len(arr) -1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, indexing):
            if arr[i] > arr[i + 1]:
                sorted = False
                #swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
            