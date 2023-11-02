
def ternarysearch(arr, target):
    left = 0 
    right = len(arr)
    
    while left <= right:
        mid1 = left + (right - left)//3 
        mid2 = right - (right - left)//3 
        if arr[mid1] == target :
            return mid1
        elif arr[mid2] == target:
            return mid2 
        elif arr[mid1] > target : 
            right = mid1-1
        elif arr[mid2] < target : 
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1 
    return -1

arr = [2, 5, 9, 33, 56, 71, 82, 99]
target = 99
result = ternarysearch(arr, target)
print(result)