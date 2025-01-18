def binarySearch(nums, target):
    def helper(nums, target, left, right):
        if left > right:
            return -1
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return helper(nums, target, left, middle - 1)
        else:
            return helper(nums, target, middle + 1, right)
    return helper(nums, target, 0, len(nums) - 1)

print(binarySearch([2,3,4,6,7,8,9], 3))