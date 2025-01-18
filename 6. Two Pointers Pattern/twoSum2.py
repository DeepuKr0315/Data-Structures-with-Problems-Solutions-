# problem link = https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        currSum = nums[left] + nums[right]
        if target == currSum:
            return [left + 1, right + 1]
        elif target < currSum:
            left += 1
        else:
            right -= 1
    return [-1, -1]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))