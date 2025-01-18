
# problem link ==> https://leetcode.com/problems/partition-equal-subset-sum/description/

def canPartition(nums):
    n = len(nums)
    if sum(nums) % 2 != 0:return False
    target = sum(nums) // 2
    prev = [False] * (target+1)
    curr = [False] * (target+1)
    prev[0] = True
    curr[0] = True
    for i in range(1, n+1):
        for j in range(1, target+1):
            #pick
            if nums[i-1] <= j:
                curr[j] = prev[j-nums[i-1]]
            else:
                curr[j] = False
            # don't pick
            curr[j] = curr[j] or prev[j]
        prev = curr[:]
    return curr[target]

nums = [1,2,3,5]
print(canPartition(nums))