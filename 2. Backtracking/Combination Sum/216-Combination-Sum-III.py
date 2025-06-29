
# problem = https://leetcode.com/problems/combination-sum-iii/description/

def combinationsSum3(n, k):
    res = []
    def helper(start, curr, currSum):
        if currSum > n:
            return
        if currSum == n:
            if len(curr) == k:
                res.append(curr[:])
                return
        hash = {}
        for j in range(start, 10):
            if j not in hash:
                hash[j] = True
                curr.append(j)
                helper(j+1, curr, currSum+j)
                curr.pop()
    helper(1, [], 0)
    return res

print(combinationsSum3(7, 3))