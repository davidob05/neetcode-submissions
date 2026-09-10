class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0] * ((len(tokens) + 1) // 2)
        top = 0

        for token in tokens:
            if len(token) == 1 and token in "+-*/":
                top -= 1
                b = stack[top]
                a = stack[top - 1]
                if token == "+":
                    stack[top - 1] = a + b
                elif token == "-":
                    stack[top - 1] = a - b
                elif token == "*":
                    stack[top - 1] = a * b
                else:
                    stack[top - 1] = int(a / b)
            else:
                stack[top] = int(token)
                top += 1

        return stack[0]