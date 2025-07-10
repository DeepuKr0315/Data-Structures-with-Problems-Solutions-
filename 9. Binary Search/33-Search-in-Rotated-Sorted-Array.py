
# problem link = https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def rotatedSearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            if nums[left] <= target and target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[middle] < target and target <= nums[right]: 
                left = middle + 1
            else:
                right = middle - 1
    return -1   

print(rotatedSearch([4,5,6,7,0,1,2], 0))