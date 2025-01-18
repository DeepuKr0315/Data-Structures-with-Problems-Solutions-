
# problem statement = https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def firstLastOccurance(nums, target):
    range = [-1, -1]
    find_Left_Extreme(nums, target, range, 0, len(nums)-1)
    find_Right_Extreme(nums, target, range, 0, len(nums)-1)
    return range

def find_Left_Extreme(array, target, range, left, right):
    if left > right:
        return
    middle = (left + right)//2
    if array[middle] == target:
        if middle == 0:
            range[0] = 0
        elif array[middle - 1] == target:
           find_Left_Extreme(array, target, range,  left, middle - 1)
        else:
            range[0] = middle
    elif target < array[middle]:
        find_Left_Extreme(array, target, range, left, middle - 1)
    else:
        find_Left_Extreme(array, target, range, middle + 1, right)

def find_Right_Extreme(array, target, range, left, right):
    if left > right:
        return
    middle = (left + right) // 2
    if array[middle] == target:
        if middle == len(array)-1:
            range[1] = middle
        elif array[middle + 1] == target:
            find_Right_Extreme(array, target, range, middle + 1, right)
        else:
            range[1] = middle
    elif target < array[middle]:
        find_Right_Extreme(array, target, range, left, middle - 1)
    else:
        find_Right_Extreme(array, target, range, middle + 1, right)

print(firstLastOccurance(nums = [5,7,7,8,8,10], target = 8))