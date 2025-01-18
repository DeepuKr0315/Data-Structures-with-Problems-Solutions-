# problem link =https://leetcode.com/problems/longest-increasing-subsequence/description/

def lengthOfLIS(nums):
    def binSearch(sub, num):
        left, right = 0, len(sub)-1
        while left < right:
            mid = (left+right) // 2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left
    sub = [nums[0]]
    n = len(nums)
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            index = binSearch(sub, num)
            # index = value in sub which >= num
            sub[index] = num
    return len(sub)

nums = [68,2343,2344,2345,2346,2347,2348,2349,2350,2351]
print(lengthOfLIS(nums))