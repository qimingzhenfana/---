def sort(arr):
    low = 0
    l = len(arr)
    for j in range(0, l):
        if arr[j] & 1 == 1:
            tmp = arr[j]
            for k in range(j-1, low-1, -1):
                arr[k + 1] = arr[k]
            arr[low] = tmp
            low += 1
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort(arr))
