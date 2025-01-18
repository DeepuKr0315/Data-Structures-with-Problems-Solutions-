def knapSack(W, wt, val):
    n = len(val)
    prev = [0]*(W+1)
    curr = [0]*(W+1)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i-1] <= j:
                include = val[i-1] + dp[i][j-wt[i-1]]
            curr[j] = max(include, exclude)
        prev = curr[:]
    return curr[W]

val = [2, 3, 10]
wt = [8, 2, 3]
print("Max items ==> ",knapSack(9, wt, val))