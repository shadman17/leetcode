class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def func(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                return int(a / b)

        stack = []
        for token in tokens:

            if token == "+" or token == "-" or token == "*" or token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(func(y, x, token))
            else:
                stack.append(int(token))

        return stack[0]
