# Problem link == https://leetcode.com/problems/edit-distance/description/

def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(0,n+1):
        dp[i][0] = i
    for j in range(0, m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                replace = 1 + dp[i-1][j-1]
                delete = 1 + dp[i-1][j]
                insert = 1 + dp[i][j-1]
                dp[i][j] = min(replace, insert, delete)
    return dp[n][m]
word1 = "dinitrophenylhydrazine"
word2 = "acetylphenylhydrazine"
print(minDistance(word1, word2))