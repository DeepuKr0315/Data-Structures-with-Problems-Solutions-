def canJump(nums):
    return canJumpFrom(0, nums)

def canJumpFrom(position, nums):
    if position == len(nums)-1:
        return True
    furthest_jump = min(position+nums[position], len(nums)-1)
    for next_pos in range(position+1, furthest_jump+1):
        if canJumpFrom(next_pos, nums):
            return True
    return False

nums = [1, 3, 0, 0, 0, 1, 2]
print(canJump(nums))