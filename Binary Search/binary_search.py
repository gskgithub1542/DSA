def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        print(start, end)
        mid = (start + end) // 2
        if target == arr[mid]:
            return arr[mid], "-", mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid
    return "Not Found"


arr = [-42, -2, 5, 7, 23, 87, 509]
target = 509
print(binary_search(arr, target))
