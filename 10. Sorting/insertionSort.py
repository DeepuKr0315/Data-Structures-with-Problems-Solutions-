# Insertion Sort
def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i-1
        temp = nums[i]
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums
print(insertionSort([5, 3, 4, 8, 1]))