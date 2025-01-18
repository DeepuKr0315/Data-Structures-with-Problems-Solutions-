
# problem link ==> https://leetcode.com/problems/palindrome-partitioning-ii/description/

def minCut(s):
    n = len(s)
    isPalindrome = [[0]*n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                isPalindrome[i][j] = True
            elif s[i] == s[j] and (j == i+1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False

    dp = [[None]*n for _ in range(n)]

    def partitions(start, end):
        if start == end or isPalindrome[start][end]:
            return 0
        if dp[start][end] is not None:
            return dp[start][end]
        minimum = end - start
        for end_index in range(start, end):
            if isPalindrome[start][end_index]:
                minimum = min(minimum, 1+partitions(end_index+1, end))
        dp[start][end] = minimum
        return dp[start][end]
    return partitions(0, n-1)

s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
print(minCut(s))