# Problem link ==> https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

def matrixMultiplication(N, arr):
    dp = [[-1]*N for _ in range(N)]
    def findCost(i, j):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        cost = float('inf')
        for k in range(i, j):
            curr_cost = findCost(i, k) + findCost(k+1, j) + arr[i-1]*arr[k]*arr[j]
            cost = min(cost, curr_cost)
            dp[i][j] = cost
        return dp[i][j]
    return findCost(1, N-1)

N = 4
nums = [10, 30, 5, 60]
print(matrixMultiplication(N, nums))