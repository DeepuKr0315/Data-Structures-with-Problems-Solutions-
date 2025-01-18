
# Problem discription = https://leetcode.com/problems/permutations/description/
# Not work for repeatition of elements in the array

def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        # base case
        if index == n-1:
            res.append(nums[:])
            return
        for j in range(index, n):
            nums[index], nums[j] = nums[j], num5s[index]
            helper(index+1)
            nums[index], nums[j] = nums[j], nums[index]
    helper(0)
    return res

print(permute([1,2,3]))