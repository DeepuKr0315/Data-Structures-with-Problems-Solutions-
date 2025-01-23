
#problem link = https://leetcode.com/problems/find-the-duplicate-number/description/

def findDuplicates(nums):
    hare = 0
    tortoise = 0
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
            pointer = 0
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]        
            return pointer

print(findDuplicates(nums = [1,3,4,2,2]))