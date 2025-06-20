
# problem link ==> https://leetcode.com/problems/longest-palindromic-substring/description/

def longestPalindrome(s):
    n = len(s)
    longest = s[0]
    dp = [[0]*(n) for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i+1 or dp[i+1][j-1]):
                dp[i][j] = True
            else:
                dp[i][j] = False
            if dp[i][j]:
                longest = s[i:j+1]
    return longest

s = "babad"
print(longestPalindrome(s))

# 2 pointers approach
def longestPalindromeTwoPointers(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]
    longest = ""
    for i in range(len(s)):
        # odd length in palindrome
        odd_palindrome = expand(i, i)
        if len(odd_palindrome)  > len(longest):
            longest = odd_palindrome
        # even length palindrome
        even_palindrome = expand(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest

s = "babad"
print(longestPalindromeTwoPointers(s))