def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    for i in range(n):
        if dp[i]:
            farthest = min(i + nums[i], n-1)
            for j in range(i+1, farthest+1):
                dp[j] = True
    return dp[-1]

nums = [1, 3, 0, 0, 1, 1, 2]
print(canJump(nums))