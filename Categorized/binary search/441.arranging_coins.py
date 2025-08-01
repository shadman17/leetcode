import math

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         return int(-1 + math.sqrt(1 + 8 * n)) // 2


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h = 1, n
        ans = 0
        while l <= h:
            mid = l + (h - l) // 2

            res = (mid / 2) * (mid + 1)

            if res > n:
                h = mid - 1

            else:
                l = mid + 1
                ans = max(ans, mid)

        return ans
