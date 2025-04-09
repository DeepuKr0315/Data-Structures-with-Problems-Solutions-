# 3375. Minimum Operations to Make Array Values Equal to K
# problem link = https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

def minOperations(nums, k):
    for num in nums:
        if num < k:
            return -1
    is_equal = True
    
    for num in nums:
        if num != k:
            is_equal = False
            break
    if is_equal:
        return 0
    greater = set()
    for num in nums:
        if num > k:
            greater.add(num)
    return len(greater)

nums = [5,2,5,4,5]
k = 2
print(minOperations(nums, k))