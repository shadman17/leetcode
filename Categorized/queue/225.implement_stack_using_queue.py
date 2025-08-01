class myQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def front(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]

    def empty(self) -> bool:
        return self.queue == []

    def size(self) -> int:
        return len(self.queue)


class MyStack:

    def __init__(self):
        self.queue1 = myQueue()
        self.queue2 = myQueue()

    def push(self, x: int) -> None:
        self.queue2.enqueue(x)

        while not self.queue1.empty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.dequeue()

    def top(self) -> int:
        return self.queue1.front()

    def empty(self) -> bool:
        return self.queue1.empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
obj.push(4)
obj.push(5)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
