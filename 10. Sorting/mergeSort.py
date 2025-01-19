<<<<<<< HEAD
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums)//2
    leftSide = mergeSort(nums[:middle])
    rightSide = mergeSort(nums[middle:]) 
    return merge(leftSide, rightSide)

def merge(nums1, nums2):
    mergedArr = []
    i, j = 0, 0
    m = len(nums1)
    n = len(nums2)
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            mergedArr.append(nums1[i])
            i += 1
        else:
            mergedArr.append(nums2[j])
            j += 1
    while i < m:
        mergedArr.append(nums1[i])
        i += 1
    while j < n:
        mergedArr.append(nums2[j])
        j += 1
    return mergedArr

=======
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums)//2
    leftSide = mergeSort(nums[:middle])
    rightSide = mergeSort(nums[middle:]) 
    return merge(leftSide, rightSide)

def merge(nums1, nums2):
    mergedArr = []
    i, j = 0, 0
    m = len(nums1)
    n = len(nums2)
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            mergedArr.append(nums1[i])
            i += 1
        else:
            mergedArr.append(nums2[j])
            j += 1
    while i < m:
        mergedArr.append(nums1[i])
        i += 1
    while j < n:
        mergedArr.append(nums2[j])
        j += 1
    return mergedArr

>>>>>>> eca4169 (adding sorting files)
print(mergeSort([5,4,3,2,1]))