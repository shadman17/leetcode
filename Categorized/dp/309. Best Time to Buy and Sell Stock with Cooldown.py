from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def memoization(ind, n, buy, dp):
            if ind == n or ind == n + 1:
                return 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            profit = 0
            if buy:
                profit = max(
                    (-prices[ind] + memoization(ind + 1, n, 0, dp)),
                    (memoization(ind + 1, n, 1, dp)),
                )
            else:
                profit = max(
                    (
                        prices[ind] + memoization(ind + 2, n, 1, dp),
                        memoization(ind + 1, n, 0, dp),
                    )
                )
            dp[ind][buy] = profit
            return dp[ind][buy]

        n = len(prices)
        return memoization(0, n, 1, [[-1] * 2 for _ in range(n)])


# Tabulation
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(
                        -prices[ind] + dp[ind + 1][0],
                        dp[ind + 1][1],
                    )
                else:
                    profit = max(
                        prices[ind] + dp[ind + 2][1],
                        dp[ind + 1][0],
                    )
                dp[ind][buy] = profit
        print(dp)
        return dp[0][1]


s = Solution()
print(s.maxProfit([1, 2, 3, 0, 2]))
