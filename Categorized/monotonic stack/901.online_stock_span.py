class StockSpanner:

    def __init__(self):
        self.stack = []
        self.ind = -1

    def next(self, price: int) -> int:
        self.ind = self.ind + 1
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        count = self.ind - (self.stack[-1][1] if self.stack else -1)
        self.stack.append((price, self.ind))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
