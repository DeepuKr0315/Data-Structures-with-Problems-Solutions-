def knapSack(W, wt, val):
    n = len(val)
    prev = [0]*(W+1)
    curr = [0]*(W+1)

    for i in range(1, n+1):
        for j in range(1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i-1] <= j:
                include = val[i-1] + prev[j-wt[i-1]]
            curr[j] = max(include, exclude)
        prev = curr[:]
    return curr[W]

val = [2, 3, 9]
wt = [8, 2, 5]
print("Max items ==> ",knapSack(8, wt, val))