
# Problem link ==> https://leetcode.com/problems/palindrome-partitioning-ii/description/

def minCut(s):
    n = len(s)
    dp = [[None]*n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i==j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i+1 or dp[i+1][j-1]):
                dp[i][j] = True
    cuts = [0]*n
    for end in range(n):
        min_cuts = end
        for start in range(end+1):
            if dp[start][end]:
                if start == 0:
                    min_cuts = 0
                else:
                    min_cuts = min(min_cuts, 1 + cuts[start-1])
        cuts[end] = min_cuts
    return cuts[n-1]

s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
print(minCut(s))