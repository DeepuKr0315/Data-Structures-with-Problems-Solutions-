# Problem link ==> https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

def matrixMultiplication(N, arr):
    dp = [[0]*N for _ in range(N)]
    for l in range(1, N+1):
        for i in range(1, N-l+1):
            j = i+l-1
            if i==j:
                dp[i][j] = 0
            else:
                cost = float('inf')
                for k in range(i, j):
                    curr_cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    cost = min(curr_cost, cost)
                dp[i][j] = cost
    return dp[1][N-1]

N = 4
nums = [10, 30, 5, 60]
print(matrixMultiplication(N, nums))