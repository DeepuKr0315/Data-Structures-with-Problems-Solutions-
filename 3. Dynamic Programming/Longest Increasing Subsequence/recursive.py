
# problem link =https://leetcode.com/problems/longest-increasing-subsequence/description/

def lengthOfLIS(nums):
    n = len(nums)
    def helper(curr, prev):
        if curr > n-1:
            return 0
        include = 0
        exclude = helper(curr+1, prev)
        if nums[curr] > nums[prev] or prev == -1:
            include = 1 + helper(curr+1, curr)
        return max(include, exclude)
    return helper(0, -1)

nums = [68,2343,2344,2345,2346,2347,2348,2349,2350,2351]
print(lengthOfLIS(nums))