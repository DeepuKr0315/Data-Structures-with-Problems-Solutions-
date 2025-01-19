def partition(array, start=0, end=None):
    if end is None:
        end = len(array)-1
    middle = (start + end)//2
    array[start], array[middle] = array[middle], array[start]
    pivot = array[start]
    i, j = start + 1, end
    while i <= j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    array[start], array[j] = array[j], array[start]
    return j


def quickSort(array, start=0, end=None):
    if end is None:
        end = len(array)-1
    while start < end:
        pivot_idx = partition(array, start, end)
        if pivot_idx - start < end - pivot_idx:
            quickSort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quickSort(array, pivot_idx + 1, end)
            end = pivot_idx - 1
    return array

print(quickSort([5,4,3,2,7,8,9]))