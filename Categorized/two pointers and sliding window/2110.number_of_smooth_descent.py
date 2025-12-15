class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        l, r = 0, 1
        count = 1
        while r < n:
            if prices[r - 1] - 1 == prices[r]:
                count += (r - l + 1)
            else:
                while l < r:
                    l += 1
                count += 1

            r += 1
        return count
             


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        l, r = 0, 1
        count = 1
        result = 1
        while r < n:
            if prices[r - 1] - 1 == prices[r]:
                count += 1
            else:
                count = 1

            result += count
            r += 1
        return result
             