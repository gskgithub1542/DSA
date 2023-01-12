def bubble_sort(arr):
    minus = 1
    for j in range(len(arr)-minus):
        for i in range(len(arr)-minus):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        minus += 1
    print(arr)
    return arr


arr = [9541, 687, 654, 987, 54, 321, 654, 987, 98465, 4198735, 7487, 987]
bubble_sort(arr)
