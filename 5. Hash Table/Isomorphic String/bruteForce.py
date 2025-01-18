# Problem link = https://leetcode.com/problems/isomorphic-strings/

def isomorphicStr(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and t[i] != t[j]:
                return False
            if s[i] != s[j] and t[i] == t[j]:
                return False
    return True

s = "bbbaaaba"
t = "aaabbbba"
print(isomorphicStr(s, t))