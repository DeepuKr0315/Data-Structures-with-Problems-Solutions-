# Problem Link = https://leetcode.com/problems/candy/description/

def candy(ratings):
    n = len(ratings)
    result = [1] * n
    # First pass: left to right
    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            result[i] = result[i - 1] + 1
    # Second pass: right to left
    for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            result[i] = max(result[i + 1] + 1, result[i])
    return sum(result)

# Example usage
ratings = [1, 0, 2]
print(candy(ratings))