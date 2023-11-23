def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Test 
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(test_arr)
print("Sorted :", test_arr)
# Sorted : [11, 12, 22, 25, 34, 64, 90] Result