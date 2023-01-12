def SelectionSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


arr = [9, 2, 6, 5, 1, 3, 1]
SelectionSort(arr)
