# Problem link = https://leetcode.com/problems/4sum/description/

def fourSum(nums, target):
    nums.sort()
    res = []
    quad = []
    def helper(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                helper(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append(quad + [nums[left], nums[right]])
                left_val = nums[left]
                right_val = nums[right]
                while left < right and left_val == nums[left]:
                    left += 1
                while left < right and right_val == nums[right]:
                    right -= 1
    helper(4, 0, target)
    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))