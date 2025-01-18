
# problem link = https://cses.fi/problemset/task/1621
import sys
def distinctNum(nums):
    # check = {}
    # count = 0
    # for num in nums:
    #     if num not in check:
    #         check[num] = 1 + check.get(num, 0)
    #         count += 1
    # return count
    # return len(set(nums))
    seen = set()
    for num in nums:
        seen.add(num)
    return len(seen)
input = sys.stdin.read
data = input().split()
nums = data[1:] 
print(distinctNum(nums))