# PROBLEM LINK = https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13
# 1922. Count Good Numbers

def countGoodNUmbers(n):
    MOD = 10 ** 9 + 7
    def pow(x, n):
        if n == 0:
            return 1
        res = 1
        while n > 1:
            if n % 2:
                res = (res * x) % MOD
            n = n // 2
            x = (x * x) % MOD
        return res * x

    even = (n + 1) // 2
    odd = n // 2
    return (pow(5, even) * pow(4, odd)) % MOD