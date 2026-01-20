from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def memoization(ind, buy, count, dp):
            if ind == len(prices) or count == 4:
                return 0

            if dp[ind][buy][count] != -1:
                return dp[ind][buy][count]

            profit = 0
            if buy:
                take = -prices[ind] + memoization(ind + 1, 0, count + 1, dp)  # buy
                skip = memoization(ind + 1, 1, count, dp)  # do nothing
                profit = max(take, skip)

            else:
                take = prices[ind] + memoization(ind + 1, 1, count + 1, dp)  # sell
                skip = memoization(ind + 1, 0, count, dp)  # do nothing
                profit = max(take, skip)

            dp[ind][buy][count] = profit

            return dp[ind][buy][count]

        dp = [
            [[-1 for _ in range(5)] for _ in range(2)] for _ in range(len(prices) + 1)
        ]

        return memoization(0, 1, 0, dp)


# Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 5 for _ in range(2)] for _ in range(n + 1)]

        for i in range(5):
            dp[n][0][i] = 0
            dp[n][1][i] = 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for count in range(3, -1, -1):
                    profit = 0
                    if buy:
                        take = -prices[ind] + dp[ind + 1][0][count + 1]  # buy
                        skip = dp[ind + 1][1][count]  # do nothing
                        dp[ind][buy][count] = max(take, skip)
                    else:
                        take = prices[ind] + dp[ind + 1][1][count + 1]  # sell
                        skip = dp[ind + 1][0][count]  # do nothing
                        dp[ind][buy][count] = max(take, skip)

        return dp[0][1][0]


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
