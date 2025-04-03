def rotate_array(nums, k):

    def helper(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    
    k = k % len(nums)
    helper(0, len(nums)-1)
    helper(0, k - 1)
    helper(k, len(nums) - 1)
    return nums

print(rotate_array([6, 8, 1, 4, 9], 2))