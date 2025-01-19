
# problem link = https://leetcode.com/problems/merge-sorted-array/submissions/1513428933/

def merge(nums1, m, nums2, n):
    mergedArr = []
    i, j = 0, 0
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
    for i in range(len(mergedArr)):
        nums1[i] = mergedArr[i]

    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))