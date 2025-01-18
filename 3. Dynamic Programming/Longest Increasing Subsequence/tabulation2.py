#### 1 DIMENSIONAL APPROACH FOR TABULATION
# problem link ==> https://leetcode.com/problems/longest-increasing-subsequence/description/

def lengthOfLis(nums):
    n = len(nums)
    dp = [1] * (n)
    max = 1
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] > max:
            max = dp[i]
    return max
nums = [68,2343,2344,2345,2346,2347,2348,2349,2350,2351]
print(lengthOfLis(nums))