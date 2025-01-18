def canJump(nums):
    memo = [None] * len(nums)
    memo[-1] = True # The last index is always reachable from itself
    def canJumpFrom(position):
        if memo[position] is not None:
            return memo[position]
        furthest_jump = min(position + nums[position], len(nums)-1)
        for next_pos in range(position + 1, furthest_jump+1):
            if canJumpFrom(next_pos):
                memo[position] = True
                return True
        memo[position] = False
        return False
    return canJumpFrom(0)

nums = [1, 3, 0, 0, 0, 1, 2]
print(canJump(nums))