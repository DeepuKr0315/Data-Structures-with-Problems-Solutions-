
# Problem = https://leetcode.com/problems/combinations/description/

def combinations(n, k):
    res=[]
    def helper(start, current):
        if len(current)==k:
            res.append(current[:])
            return
        for j in range(start, n+1):
            current.append(j)
            helper(j+1, current)
            current.pop()
    helper(1, [])
    return res

print(combinations(4, 2))