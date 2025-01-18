# problem link = https://leetcode.com/problems/repeated-dna-sequences/description/

def dnaSequence(s):
    seen, output = set(), set()
    L = 10
    n = len(s)
    for start in range(n-L+1):
        temp = s[start:start + L]
        if temp in seen:
            output.add(temp)
        seen.add(temp)
    return list(output)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(dnaSequence(s))