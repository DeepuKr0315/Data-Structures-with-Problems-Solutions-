# problem link = https://leetcode.com/problems/repeated-dna-sequences/description/

def dnaSequence(s):
    L = 10
    n = len(s)
    if n <= L:
        return []
    to_int = {"A":0, "C":1, "G":2, "T":3}
    nums = [to_int.get(s[i]) for i in range(n)]
    a = 4
    aL = pow(a, L)
    h = 0
    output, seen = set(), set()
    for start in range(n-L+1):
        if start != 0:
            h = h * a - nums[start - 1] * aL + nums[start + L - 1]
        else:
            for i in range(L):
                h = h * a + nums[i]
        if h in seen:
            output.add(s[start:start+L])
        seen.add(h)
    return list(output)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(dnaSequence(s))