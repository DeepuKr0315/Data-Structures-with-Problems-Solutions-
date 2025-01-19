def bubbleSort(nums):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(nums)-1-counter):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted = False
    return nums

print(bubbleSort([5, 4, 3, 2, 1]))