# 2698. Find the Punishment Number of an Integer
# problem link = https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

def punishmentNumber(n):
    def canPartition(s, target, index, currSum):
        if index == len(s):
            return currSum == target
        num = 0
        for i in range(index, len(s)):
            num = num * 10 + int(s[i])
            if currSum + num > target:
                break
            if canPartition(s, target, i + 1, currSum + num):
                return True
        return False
    punishmentSum = 0
    for i in range(1, n+1):
        sqr_str = str(i * i)
        if canPartition(sqr_str, i, 0, 0):
            punishmentSum += i * i
    return punishmentSum

print(punishmentNumber(10))