def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j >= 0:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i -= 1
                continue
            elif arr[i] > arr[j]:
                break
    print(arr)


insertion_sort()
arr = [3, 2, 5, 4, 1]
# Youtube Code

for i in range(1, len(arr)):
    j = i
    while arr[j-1] > arr[j] and j > 0:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
print(arr)
