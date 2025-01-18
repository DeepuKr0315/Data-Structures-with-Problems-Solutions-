# problem link = https://leetcode.com/problems/rotate-array/description/

def rotateArray(array, k):
    length = len(array)
    k = k % length
    temp = array[length - k:]
    for i in range(length - k - 1, -1, -1):
        array[i + k] = array[i]
    for i in range(k):
        array[i] = temp[i]
    return array

nums = [1,2,3,4,5,6,7]
k = 3
print(rotateArray(nums, k))