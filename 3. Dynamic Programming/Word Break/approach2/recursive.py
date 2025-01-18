# problem statement = https://leetcode.com/problems/word-break/description/

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False]*n
    def check(index):
        if index < 0:return True
        for word in wordDict:
            if s[index-len(word)+1:index+1] == word and check(index-len(word)):
                return True
        return False
    return check(n-1)

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))