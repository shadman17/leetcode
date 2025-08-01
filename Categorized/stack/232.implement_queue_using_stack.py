class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return self.stack == []
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack() 

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()        

    def empty(self) -> bool:
        return self.stack1.empty() and self.stack2.empty()        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.empty())


