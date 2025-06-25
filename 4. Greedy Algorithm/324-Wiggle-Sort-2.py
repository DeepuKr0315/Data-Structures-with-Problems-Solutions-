# Problem link = https://leetcode.com/problems/wiggle-sort-ii

def wiggleSort(nums):
    n = len(nums)

    def median(nums):
        sorted_nums = sorted(nums)
        return sorted_nums[n // 2]
    
    def virtual_index(idx):
        return (idx * 2 + 1) % (n | 1)
    
    median_value = median(nums)
    left = 0
    i = 0
    right = n - 1
    while i <= right:
        vi = virtual_index(i)
        v_left = virtual_index(left)
        v_right = virtual_index(right)
        if nums[vi] > median_value:
            nums[vi], nums[v_left] = nums[v_left], nums[vi]
            i += 1
            left += 1
        elif nums[vi] < median_value:
            nums[vi], nums[v_right] = nums[v_right], nums[vi]
            i += 1
            right -= 1
        else:
            i += 1
    return nums

# Example usage
nums = [1, 5, 1, 1, 6, 4]
print(wiggleSort(nums))  # Output: [1, 6, 1, 5, 1, 4] or similar valid wiggle sort order
