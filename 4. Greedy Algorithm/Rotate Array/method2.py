# problem link = https://leetcode.com/problems/rotate-array/description/

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums

def rotateArray(array, k):
    k = k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array

nums = [1, 2, 3, 4, 5, 6]
k = 2
print(rotateArray(nums, k))