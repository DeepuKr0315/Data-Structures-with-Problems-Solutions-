
# problem statement = https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def firstLastOccurance(nums, target):
    left = left_Extreme(nums, target)
    right = right_Extreme(nums, target)
    return [left, right]

def left_Extreme(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right)//2
        if nums[middle] == target:
            if middle == 0:
                return 0
            elif nums[middle - 1] == target:
                right = middle - 1
            else:
                return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def right_Extreme(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            if middle == len(nums)-1:
                return middle
            elif nums[middle + 1] == target:
                left = middle + 1
            else:
                return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return-1

print(firstLastOccurance(nums = [5,7,7,8,8,10], target = 8))