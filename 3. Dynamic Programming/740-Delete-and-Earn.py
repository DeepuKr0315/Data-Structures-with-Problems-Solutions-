# 740. Delete and Earn
# problem link = https://leetcode.com/problems/delete-and-earn/description/?envType=study-plan-v2&envId=dynamic-programming

def deleteAndEarn(nums):
    max_value = max(nums)
    points = [0] * (max_value + 1)
    for num in nums:
        points[num] += num
    dp = [0] * (max_value + 1)
    dp[0] = points[0]
    if max_value > 1:
        dp[1] = max(points[0], points[1])
    for i in range(2, max_value + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
    return dp[-1]

print(deleteAndEarn(nums = [2,2,3,3,3,4]))