# Problem link = https://leetcode.com/problems/combination-sum-iv/description

def combinationSum4(nums, target):
    memo = {}
    def helper(rem_sum):
        if rem_sum < 0:
            return 0
        if rem_sum == 0:
            return 1
        if rem_sum in memo:
            return memo[rem_sum]
        count = 0
        for num in nums:
            if rem_sum - num >= 0:
                count += helper(rem_sum - num)
        memo[rem_sum] = count
        return count
    return helper(target)

def combinationSum4_dp(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

# Example usage
nums = [1, 2, 3]
target = 4
print(combinationSum4(nums, target))  # Output: 7
print(combinationSum4_dp(nums, target))  # Output: 7