
class MinStack:

    def __init__(self):
        self.arr = []
        self.max_num = None

    def push(self, val: int) -> None:
        if self.max_num is None or val > self.max_num:
            self.max_num = val
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()
            if self.arr:
                self.max_num = max(self.arr)
            else:
                self.max_num = None

    def top(self) -> int:
        return self.max_num
        
    def getMin(self) -> int:
        return min(self.arr)
        
minStack = MinStack()
print(minStack.push(1))
print(minStack.push(2))
print(minStack.push(0))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

