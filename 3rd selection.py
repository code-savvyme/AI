def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
    return arr
    
print(selectionSort([9,56,75,4,61,26]))