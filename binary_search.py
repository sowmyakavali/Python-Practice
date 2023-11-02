
def binarysearch(arr, x):
    s = 0 
    e = len(arr)
    while s < e:
        print(e)
        mid = s + (e - s)//2
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            s = mid + 1 
        else : 
            e = mid - 1 
    
    return -10


arr = [2, 5, 7, 8, 9, 20, 25, 35, 50, 70]
x = 2
"""
#######
s = 0 , e=5
mid = 2
arr[mid] = 7 > 2 
e = 2-1 = 1

######
s = 0 e = 1
"""

print(binarysearch(arr, x))