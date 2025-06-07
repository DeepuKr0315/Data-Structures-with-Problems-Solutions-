# Problem Link = https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/

def constructDistanceSubsequence(n):
    result = [-1] * (2 * n - 1)
    used = set()
    def backtrack(idx):
        if idx == len(result):
            return True
        if result[idx] != -1:
            return backtrack(idx + 1)
        for j in range(n, 0 , -1):
            if j in used:
                continue
            if j == 1:
                if result[idx] == -1:
                    result[idx] = 1
                    used.add(1)
                    if backtrack(idx + 1):
                        return True
                    result[idx] = -1
                    used.remove(1)
            else:
                if idx + j < len(result) and result[idx] == -1 and result[idx + j] == -1:
                    result[idx] = result[idx + j] = j
                    used.add(j)
                    if backtrack(idx + 1):
                        return True
                    result[idx] =  result[idx + j] = -1
                    used.remove(j)
        return False
    backtrack(0)
    return result

print(constructDistanceSubsequence(5))
print(constructDistanceSubsequence(7))