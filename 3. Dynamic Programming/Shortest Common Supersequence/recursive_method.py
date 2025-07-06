# Problem link = https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1

def shortest_common_supersequence(s1, s2):
    def helper(idx1, idx2):
        if idx1 == len(s1):
            return len(s2) - idx2
        if idx2 == len(s2):
            return len(s1) - idx1
        if s1[idx1] == s2[idx2]:
            return 1 + helper(idx1 + 1, idx2 + 1)
        return 1 + min(helper(idx1 + 1, idx2 ), helper(idx1, idx2 + 1))
    return helper(0, 0)

# Example usage
s1 = "geek"
s2 = "eke"
print("Length of Shortest Common Supersequence is", shortest_common_supersequence(s1, s2))
# Output: Length of Shortest Common Supersequence is 9