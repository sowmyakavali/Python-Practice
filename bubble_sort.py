def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                n = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = n                
            else:
                arr[j] = arr[j]
                arr[j+1] = arr[j+1]
    return arr 

arr = [9, 2, 4, 0, 33, 5, 99]
results = bubblesort(arr)
print(results)