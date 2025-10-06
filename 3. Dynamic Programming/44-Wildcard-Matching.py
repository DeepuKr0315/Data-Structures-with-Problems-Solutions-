# Problem link = https://leetcode.com/problems/wildcard-matching/

def isMtach_recursion(s1, s2):
    def helper(idx1, idx2):
        if idx1 == len(s1) and idx2 == len(s2):
            return True
        if idx2 == len(s2):
            return False
        if idx1 == len(s1):
            for i in range(idx2, len(s2)):
                if s2[i] != '*':
                    return False
            return True
        if s1[idx1] == s2[idx2] or s2[idx2] == '?':
            return helper(idx1 + 1, idx2 + 1)
        if s2[idx2] == '*':
            return helper(idx1 + 1, idx2) or helper(idx1, idx2 + 1)
        return False
    return helper(0, 0)