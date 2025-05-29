# Problem link = https://leetcode.com/problems/next-permutation/description/

def nextPermutation(nums):
    def reverse(start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    n = len(nums)
    idx = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            idx = i
            break
    if idx == -1:
        reverse(0, n - 1)
        return
    for i in range(n - 1, idx, -1):
        if nums[i] > nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
            break
    reverse(idx + 1, n - 1)

nums = [1,1,5]
nextPermutation(nums)
print(nums)