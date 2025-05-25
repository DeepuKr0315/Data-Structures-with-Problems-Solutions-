# Prolem link = https://leetcode.com/problems/3sum/description/

# by sorting the input array
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i == 0 or nums[i-1] != nums[i]: #skips the repeated elements
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right] + nums[i]
                if 0 == currSum:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
    return res

print(threeSum(nums = [-1,0,1,2,-1,-4]))