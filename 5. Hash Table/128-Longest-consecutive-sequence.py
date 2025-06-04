# Problem link = https://leetcode.com/problems/longest-consecutive-sequence/description/

def longestConsecutive(nums):
    nums.sort()
    max_consecutive = 1
    current_max = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        elif nums[i] == nums[i - 1] + 1:
            current_max += 1
        else:
            max_consecutive = max(max_consecutive, current_max)
            current_max = 1
    return max(max_consecutive, current_max)

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))