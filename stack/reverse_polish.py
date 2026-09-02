# ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for i in tokens:
            if i not in ["+", "*", "-", "/"]:
                my_stack.append(i)
            elif i == "+":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) + int(num1))
            elif i == "-":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) - int(num1))
            elif i == "*":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) * int(num1))
            elif i == "/":
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.append(int(num2) / int(num1))

        return my_stack[0]
        #     print(my_stack)
        # print(my_stack)

sol = Solution()

print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(sol.evalRPN(["1","2","+","3","*","4","-"]))
print(sol.evalRPN(["18"]))
