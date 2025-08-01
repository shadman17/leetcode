class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefix = []
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        x = self.prefix[right]
        y = self.prefix[left - 1] if left > 0 else 0
        return (x-y)