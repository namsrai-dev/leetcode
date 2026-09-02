
class MinStack:

    def __init__(self):
        self.arr = []
        self.min_num = None

    def push(self, val: int) -> None:
        if self.min_num is None or val < self.min_num:
            self.min_num = val
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()
            if self.arr:
                self.min_num = min(self.arr)
            else:
                self.min_num = None

    def top(self) -> int:
        return self.arr[-1] if self.arr else None

    def getMin(self) -> int:
        return self.min_num
        
minStack = MinStack()
print(minStack.push(1))
print(minStack.push(2))
print(minStack.push(-2))
print(minStack.push(-1))
print(minStack.push(-2))
print(minStack.push(3))
print(minStack.pop())
print(minStack.getMin())
print(minStack.top())
print(minStack.getMin())

