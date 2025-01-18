# Problem link = https://leetcode.com/problems/isomorphic-strings/

def isomorphicStr(s, t):
    if len(s) != len(t):
        return False
    sHash = {}
    tHash = {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s not in sHash:
            sHash[char_s] = char_t
        if char_t not in tHash:
            tHash[char_t] = char_s
        if sHash[char_s] != char_t or tHash[char_t] != char_s:
            return False
    return True

s = "bbbaaaba"
t = "aaabbbba"
print(isomorphicStr(s, t))