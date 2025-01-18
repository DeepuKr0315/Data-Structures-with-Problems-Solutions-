def maxUniqueLength(s):
    seen = {}
    start, maxLen = 0, 0
    for i in range(len(s)):
        if s[i] in seen:
            start = max(start, seen[s[i]] + 1)
        maxLen = max(maxLen, i - start + 1)
        seen[s[i]] = i
    return maxLen

print(maxUniqueLength("pqbrstbuvwpvy"))