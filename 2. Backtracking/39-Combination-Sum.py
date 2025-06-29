
# Problem = https://leetcode.com/problems/combination-sum/description/

def combinationSum(candidates, target):
    res = []
    n = len(candidates)
    def helper(start, curr, sum_included):
        # base case
        if sum_included>target:
            return
        if sum_included == target:
            res.append(curr[:])
            return
        
        # recursive case
        for j in range(start, n):
            curr.append(candidates[j])
            helper(j, curr, sum_included+candidates[j])
            curr.pop()

    helper(0, [], 0)
    return res

print(combinationSum([2,3,4,7],7))