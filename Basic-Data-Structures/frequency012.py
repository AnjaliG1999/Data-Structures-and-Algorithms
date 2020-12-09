def frequency1(arr):
    n = len(arr)
    count = [0, 0, 0]

    for key in arr:
        count[key] += 1
    
    sortedArr = [None] * n

    for val in range(count[0]):
        sortedArr[val] = 0
    
    for val in range(count[0], count[1]+count[0]):
        sortedArr[val] = 1
    
    for val in range(count[1]+count[0], n):
        sortedArr[val] = 2

    return sortedArr

def frequency2(arr):
    index1 = 0
    sortedArr = []

    for key in arr:
        if key == 2:
            sortedArr.append(key)
        elif key == 1:
            sortedArr.insert(index1, key)
            index1 += 1
        else:
            sortedArr.insert(0, key)
            index1 += 1

    return sortedArr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# print(frequency1(arr))
print(frequency2(arr))