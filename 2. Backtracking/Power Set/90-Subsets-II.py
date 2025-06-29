
# Problem = https://leetcode.com/problems/subsets-ii/description/

def subsetsWithDup(nums):
    res=[]
    nums.sort()
    def helper(index, current):
        if index == len(nums):
            res.append(current[:])
            return
        
        #include choice
        current.append(nums[index])
        helper(index+1, current)
        current.pop() #backtracking

        # exclude choice
        while index<len(nums)-1 and nums[index] == nums[index+1]:
            index += 1
        helper(index+1, current)

    helper(0, [])
    return res

print(subsetsWithDup([4, 4, 4, 1, 4])[::-1])