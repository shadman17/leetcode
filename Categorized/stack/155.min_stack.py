class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
        if self.min_stack:
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack, obj.min_stack)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())