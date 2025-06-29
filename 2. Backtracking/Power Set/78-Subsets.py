
# Problem = https://leetcode.com/problems/subsets/description/

def powerSet(nums):
    res = []
    def helper(nums, index, subset):
        if index == len(nums):
            res.append(subset.copy())
            return
        helper(nums, index+1, subset)
        subset.append(nums[index])
        helper(nums, index+1, subset)
        subset.pop()
    helper(nums, 0, [])
    return res

print(powerSet([1,8,7]))