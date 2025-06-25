# problem link = https://leetcode.com/problems/jump-game-ii/description/

def canJump2(nums):
    n = len(nums)
    if n == 1:
        return 0
    jump = 0
    current_max = 0
    next_max = 0
    for i in range(n-1):
        next_max = max(next_max, i + nums[i])
        if current_max == i:
            jump += 1
            current_max = next_max
            if current_max >= n-1:
                return jump
    return jump

nums = [2,3,1,1,4]
print(canJump2(nums))

# Output = 2 ==> 
# The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.