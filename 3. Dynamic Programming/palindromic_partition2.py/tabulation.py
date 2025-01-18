
# Problem link ==> https://leetcode.com/problems/palindrome-partitioning-ii/description/

def minCut(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i==j:
                dp[i][j] = 0
            elif s[i]==s[j] and (j == i+1 or dp[i+1][j-1]==0):
                dp[i][j] = 0
            else:
                dp[i][j] = j-1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+1+dp[k+1][j])
    return dp[0][n-1]

s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
print(minCut(s))