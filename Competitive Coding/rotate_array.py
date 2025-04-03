def rotate_array(nums, k):

    def rotate(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
    
    k = k % len(nums)
    rotate(0, len(nums)-1)
    rotate(0, k - 1)
    rotate(k, len(nums) - 1)
    return nums

print(rotate_array([6, 8, 1, 4, 9], 2))