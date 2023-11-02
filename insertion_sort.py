def InsertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i - 1 
        key = arr[i]
        while j >= 0 and arr[j] > key : 
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key 

    return arr 

arr = [31, 0, 22, 34, 1, 45, 30, 99]
print(InsertionSort(arr))