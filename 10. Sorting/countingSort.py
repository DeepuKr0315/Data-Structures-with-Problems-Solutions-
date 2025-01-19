def counting_sort(array):
    temp = [0] * 10
    output = [0] * len(array)
    # Count occurrences of each digit
    for num in array:
        temp[num] += 1

    # Cumulative count to determine positions
    for i in range(1, 10):
        temp[i] += temp[i - 1]

    # Build the output array
    for j in range(len(array) - 1, -1, -1):
        digit = array[j]
        temp[digit] -= 1
        insert_position = temp[digit]
        output[insert_position] = array[j]

    # Copy sorted array back into original array
    array[:] = output[:]
    return array

print(counting_sort([1,1,1,7,4,4,8,8,2,3,7,4]))