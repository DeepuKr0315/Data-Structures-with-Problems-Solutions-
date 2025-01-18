def canJump(nums):
    n = len(nums)
    max_index = 0
    for i in range(n):
        if i > max_index:
            return False
        max_index = max(max_index, i+nums[i])
        if max_index >= n-1:
            return True

nums = [1, 3, 0, 0, 1, 1, 2]
print(canJump(nums))