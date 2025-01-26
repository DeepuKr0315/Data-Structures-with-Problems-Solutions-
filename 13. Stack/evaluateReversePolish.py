# Problem Name = 150. Evaluate Reverse Polish Notation
# Problem Link = https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def evalRPN(tokens):
    stack = []
    valid_opr = {
        "+": lambda n1, n2: n1 + n2,
        "-": lambda n1, n2: n1 - n2,
        "*": lambda n1, n2: n1 * n2,
        "/": lambda n1, n2: int(n1 / n2) if n1 * n2 > 0 else -(-n1 // n2)
    }
    for token in tokens:
        if token in valid_opr:
            n2 = stack.pop()
            n1 = stack.pop()
            result = valid_opr[token](n1, n2)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))