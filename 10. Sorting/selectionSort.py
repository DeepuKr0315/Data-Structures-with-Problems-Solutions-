def selectionSort(nums):
    # The outer loop run n times, where n is the length of nums
    # As i increase, the nuber of times inner loop runs decreases
    # Therefore, this loop will run roughly n*(n-1)/2 times, which simplifies to O(n^2)
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        # The swap operation done in constant time O(1)
        if i != smallest:
            nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums

print(selectionSort([5, 4, 3, 2, 1]))