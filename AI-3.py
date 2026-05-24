def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Find the index of the minimum element from i to n-1
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
