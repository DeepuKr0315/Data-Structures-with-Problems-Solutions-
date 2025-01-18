# https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(s):
    balance = 0
    result = ""
    for i in range(len(s)):
        if s[i] == "(":
            balance += 1
            if balance > 1:
                result += "("
        else:
            if balance > 1:
                result += ")"
            balance -= 1
    return result

print(removeOuterParentheses("(()())"))