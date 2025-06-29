# This code help us to fnd permutation where elements are repeated

# Problem = https://leetcode.com/problems/permutations-ii/description/

def permutationUnique(nums):
    res = []
    def helper(index):
        # base case
        if len(nums)-1 == index:
            res.append(nums[:])
            return
        # here we store the value that we check if get repeated or not
        hash = {}
        # recursive case
        for j in range(index, len(nums)):
            if nums[j] not in hash:
                hash[nums[j]] = True
                nums[index], nums[j] = nums[j], nums[index]
                helper(index+1)
                nums[index], nums[j] = nums[j], nums[index]
    helper(0)
    return res

print(permutationUnique([1,1,2]))