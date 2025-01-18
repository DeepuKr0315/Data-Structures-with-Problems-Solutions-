# problem link =https://leetcode.com/problems/longest-increasing-subsequence/description/

def lengthOfLIS(nums):
    n = len(nums)
    dp = [[-1]*(n) for _ in range(n)]
    def helper(curr, prev):
        if curr > n-1:
            return 0
        if dp[curr][prev+1] != -1:
            return dp[curr][prev+1]
        
        include = 0
        exclude = helper(curr+1, prev)
        if nums[curr] > nums[prev] or prev == -1:
            include = 1 + helper(curr+1, curr)
        dp[curr][prev+1] = max(include, exclude)
        return dp[curr][prev+1]
    return helper(0, -1) # because -1 have to converted to 1 that's why we add 1 in prev index every time

nums = [68,2343,2344,2345,2346,2347,2348,2349,2350,2351]
print(lengthOfLIS(nums))