# problem statement = https://leetcode.com/problems/word-break/description/

def wordBreak(s, wordDict):
    n = len(s)
    dp = [-1]*n
    def check(index):
        if index < 0:
            return True
        if dp[index] != -1:
            return dp[index]
        for word in wordDict:
            if s[index-len(word)+1:index+1] == word and check(index-len(word)):
                dp[index] = True
                return dp[index]
        dp[index] = False
        return dp[index]
    return check(n-1)

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))