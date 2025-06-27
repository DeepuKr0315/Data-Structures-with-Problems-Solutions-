# Problem link = https://leetcode.com/problems/longest-valid-parentheses/description/

def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
    return max_len

# Example usage
s = "(()())"
print(longestValidParentheses(s))  # Output: 6