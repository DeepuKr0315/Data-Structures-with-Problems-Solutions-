# prolem link = https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

def numSubseq(nums, target):
    nums.sort()
    res = 0
    MOD = 10 ** 9 + 7
    right = len(nums) - 1
    for i, left in enumerate(nums):
        while(left + nums[right] > target) and i <= right:
            right -= 1
        if i <= right:
            res += 2 ** (right - i)
    return res % MOD

nums = [3,5,6,7]
target = 9
print(numSubseq(nums, target))