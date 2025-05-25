# Problem link = https://leetcode.com/problems/sum-of-square-numbers/description/
# 633. Sum of Square Numbers

def judgeSquareSum(num):
    def sqrt(num):
        left = 0
        right = num
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if mid * mid <= num:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    left = 0
    right = sqrt(num)
    while left <= right:
        total = left * left + right * right
        if total == num:
            return True
        elif total > num:
            right -= 1
        else:
            left += 1
    return False

c = 5
print(judgeSquareSum(c))