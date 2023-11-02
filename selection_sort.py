def Selectionsort(arr):
    for i in range(len(arr)):
        min = i 
        j = i + 1
        while j < len(arr)-1:
            if arr[min] > arr[j]:
                min = j
            j = j + 1
        arr[i], arr[min] = arr[min], arr[i]
    return arr 

def Selectionsort2(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr 

arr = [90, 40, 0, 33, 5, 88, 23, 99]
res = Selectionsort2(arr)
print("res : ", res)