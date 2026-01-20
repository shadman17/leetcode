from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def memoization(ind, n, buy, dp):
            if ind == n:
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
                        prices[ind] + memoization(ind + 1, n, 1, dp),
                        memoization(ind + 1, n, 0, dp),
                    )
                )
            dp[ind][buy] = profit
            return dp[ind][buy]

        n = len(prices)
        return memoization(0, n, 1, [[-1] * 2 for _ in range(n)])
