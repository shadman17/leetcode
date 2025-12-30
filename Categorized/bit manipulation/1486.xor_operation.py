class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        count = 0
        res = 0
        while count < n:
            res = res ^ (start + 2 * count)
            count += 1

        return res
