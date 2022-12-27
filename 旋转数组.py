def sort(arr):
    low = 1
    high = len(arr) - 1
    while low < high:
        while arr[low] & 1 == 1 and low < high:
            low += 1
        while arr[high] & 1 == 0 and low < high:
            high -= 1
        if low < high:
            tmp = arr[low]
            arr[low] = arr[high]
            arr[high] = tmp
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort(arr))
