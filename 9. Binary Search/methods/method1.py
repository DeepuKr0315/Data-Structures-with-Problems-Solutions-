def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binarySearch([2,3,4,6,7,8,9], 8))