def knapSack(W, wt, val):
    n = len(val)
    def helper(index, rem_weight):
        # base case
        if index > n-1 or rem_weight == 0:
            return 0
        # recursive case
        exclude = helper(index+1, rem_weight)
        include = 0
        if wt[index] <= rem_weight:
            include = val[index] + helper(index+1, rem_weight-wt[index])
        return max(exclude, include)
    return helper(0, W)

val = [2, 3, 9]
wt = [8, 2, 5]
print("Max items ==> ",knapSack(8, wt, val))