# problem statement = https://leetcode.com/problems/word-break/description/

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*n
    for i in range(n):
        for word in wordDict:
            if i < len(word)-1:
                continue
            elif s[i-len(word)+1:i+1] == word and (i == len(word)-1 or dp[i-len(word)]):
                dp[i] = True
                break
    return dp[n-1]

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))