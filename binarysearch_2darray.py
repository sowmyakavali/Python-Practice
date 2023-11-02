def searchin2Darray(matrix, target):

    m = len(matrix)
    n = len(matrix[0])

    left = 0 
    right = m*n -1 
    while left <= right:
        mid = left + (right - left)//2 
        mid_element = matrix[mid//2][mid%2] 
        if target == mid_element:
            return True
        elif mid_element > target:
            right = mid -1 
        else :
            left = mid + 1 
    return False


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
target = 8 
result = searchin2Darray(matrix, target)
print(result)