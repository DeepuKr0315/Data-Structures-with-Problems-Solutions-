# Problem link = https://leetcode.com/problems/lexicographical-numbers/description

def lexicographical_num(n):
    res = [] 
    def dfs(num):
        if num > n:
            return
        res.append(num)
        for i in range(10):
            if num * 10 + i > n:
                return
            dfs(num * 10 + i)
    for i in range(1, 10):
        dfs(i)
    return res

print(lexicographical_num(5))