# Problem link = https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums):
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[left] ** 2 > nums[right] ** 2:
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

# Example usage
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]