
# Problem = https://leetcode.com/problems/combination-sum-ii/description/

def combinationsSum2(candidates, target):
    candidates.sort()
    n = len(candidates)
    res = []
    def helper(start, curr, currSum):
        if currSum > target:
            return
        if currSum == target:
            res.append(curr[:])
            return
        if start > n-1:
            return
        hash = {}
        for j in range(start, n):
            if candidates[j] not in hash:
                hash[candidates[j]] = True
                curr.append(candidates[j])
                helper(j+1, curr, currSum + candidates[j])
                curr.pop()
    helper(0, [], 0)
    return res

print(combinationsSum2([3, 5, 2, 1, 3], 7))