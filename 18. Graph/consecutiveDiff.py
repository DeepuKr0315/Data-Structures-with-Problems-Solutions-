# problem link = https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# 967. Numbers With Same Consecutive Differences

def numSameConsecDiff(n, k):
    if n == 1:
        return [i for i in range(10)]
    result = []
    def dfs(num, length):
        if length == n:
            result.append(num)
            return
        last_digit = num % 10
        next_digits = set([last_digit + k, last_digit - k])
        for next_digit in next_digits:
            if 0 <= next_digit <= 9:
                new_num = num * 10 + next_digit
                dfs(new_num, length + 1)
    for i in range(1, 10):
        dfs(i, 1)
    return result

print(numSameConsecDiff(n = 3, k = 7))