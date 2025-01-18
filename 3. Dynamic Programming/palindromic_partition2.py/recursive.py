
# Problem link ==> https://leetcode.com/problems/palindrome-partitioning-ii/description/

def minCut(s):
    n = len(s)

    def isPalindrome(i, j):
        while i<j:
            if s[i]!=s[j]:return False
            i += 1
            j -= 1
        return True
    
    def partition(start, end):
        if start == end or isPalindrome(start, end):
            return 0
        minimum = end - start
        for end_index in range(start, end):
            if isPalindrome(start, end_index):
                minimum = min(minimum, 1+partition(end_index+1, end))
        return minimum

    return partition(0, n-1)

s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
print(minCut(s))