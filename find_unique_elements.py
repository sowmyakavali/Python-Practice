def findUniques(arr):
    a = {}
    for i in arr:
        if not i in list(a.keys()):
            a[i] = 1
        else:
            a[i] += 1

    # sorted_values = sorted(a.values())
    # sorted_dict = {}
    # for i in sorted_values:
    #     key = [a.keys()][sorted_values.index(i)]
    #     sorted_dict[key] = i 

    return a

arr = [1, 1, 1, 2, 3, 0, 9, 3, 3, 3] 
sa = findUniques(arr)   
print(sa)
print(list(sa.keys())[list(sa.values()).index(3)])