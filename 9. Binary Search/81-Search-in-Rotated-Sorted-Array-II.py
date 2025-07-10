# Problem link = https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False

nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))  # Output: True