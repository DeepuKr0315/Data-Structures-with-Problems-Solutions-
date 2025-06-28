# Problem link = https://leetcode.com/problems/house-robber-ii/description/

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    def rob_1(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
    return max(rob_1(nums[:-1]), rob_1(nums[1:]))

# Example usage
nums = [2, 3, 2]
print(rob(nums))  # Output: 3