# Problem link = https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

def minimizeMax(nums, p):
    nums.sort()
    left = 0
    right = nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= mid:
                count += 1
                i += 1
            i += 1
        if count >= p:
            right = mid
        else:
            left = mid + 1
    return left

# Example usage:
nums = [1, 3, 6, 19, 20]
p = 2
print(minimizeMax(nums, p))
# Explanation: The pairs (1, 3) and (19, 20) can be formed with a maximum difference of 2.

# Example usage:
nums = [1, 5, 9, 13]
p = 1
print(minimizeMax(nums, p))