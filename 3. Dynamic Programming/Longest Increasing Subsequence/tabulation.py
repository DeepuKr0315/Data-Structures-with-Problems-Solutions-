
##### 1 DIMENSIONAL APPROACH FOR TABULATION
# problem link = https://leetcode.com/problems/longest-increasing-subsequence/description/

def lengthOfLis(nums):
    n = len(nums)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(i, -1, -1):
            exclude = dp[i+1][j]
            include = 0
            if j-1 == -1 or nums[i]>nums[i-1]:
                include = 1 + dp[i+1][i+1]
            dp[i][j] = max(include, exclude)
    return dp[0][0]

nums = [68,2343,2344,2345,2346,2347,2348,2349,2350,2351]
print(lengthOfLis(nums))