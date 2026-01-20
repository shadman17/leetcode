from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def memoization(ind, buy, count, dp):
            if ind == len(prices) or count == 0:
                return 0

            if dp[ind][buy][count] != -1:
                return dp[ind][buy][count]

            profit = 0
            if buy:
                take = -prices[ind] + memoization(ind + 1, 0, count - 1, dp)  # buy
                skip = memoization(ind + 1, 1, count, dp)  # do nothing
                profit = max(take, skip)

            else:
                take = prices[ind] + memoization(ind + 1, 1, count - 1, dp)  # sell
                skip = memoization(ind + 1, 0, count, dp)  # do nothing
                profit = max(take, skip)

            dp[ind][buy][count] = profit

            return dp[ind][buy][count]

        dp = [
            [[-1 for _ in range(2 * k + 1)] for _ in range(2)]
            for _ in range(len(prices))
        ]

        return memoization(0, 1, 2 * k, dp)


# Tabulation
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (2 * k + 1) for _ in range(2)] for _ in range(n + 1)]

        profit = 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for count in range(1, 2 * k + 1):

                    if buy:
                        take = -prices[ind] + dp[ind + 1][0][count - 1]
                        skip = dp[ind + 1][1][count]
                        profit = max(take, skip)

                    else:
                        take = prices[ind] + dp[ind + 1][1][count - 1]
                        skip = dp[ind + 1][0][count]
                        profit = max(take, skip)

                    dp[ind][buy][count] = profit

        return dp[0][1][2 * k]


# Space Optimization Recursion
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def memoization(ind, count, dp):
            if ind == len(prices) or count == 0:
                return 0

            if dp[ind][count] != -1:
                return dp[ind][count]

            profit = 0
            if count % 2 == 0:
                take = -prices[ind] + memoization(ind + 1, count - 1, dp)  # buy
                skip = memoization(ind + 1, count, dp)  # do nothing
                profit = max(take, skip)

            else:
                take = prices[ind] + memoization(ind + 1, count - 1, dp)  # sell
                skip = memoization(ind + 1, count, dp)  # do nothing
                profit = max(take, skip)

            dp[ind][count] = profit

            return dp[ind][count]

        dp = [[-1] * (2 * k + 1) for _ in range(len(prices) + 1)]

        return memoization(0, 2 * k, dp)


# Space Optimization Tabulation
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * (2 * k + 1) for _ in range(n + 1)]

        profit = 0

        for ind in range(n - 1, -1, -1):
            for count in range(1, 2 * k + 1):

                if count % 2 == 0:
                    take = -prices[ind] + dp[ind + 1][count - 1]
                    skip = dp[ind + 1][count]
                    profit = max(take, skip)

                else:
                    take = prices[ind] + dp[ind + 1][count - 1]
                    skip = dp[ind + 1][count]
                    profit = max(take, skip)

                dp[ind][count] = profit

        return dp[0][2 * k]


# Space Optimization Further
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        after = [0] * (2 * k + 1)
        curr = [0] * (2 * k + 1)

        profit = 0

        for ind in range(n - 1, -1, -1):
            for count in range(1, 2 * k + 1):

                if count % 2 == 0:
                    take = -prices[ind] + after[count - 1]
                    skip = after[count]
                    profit = max(take, skip)

                else:
                    take = prices[ind] + after[count - 1]
                    skip = after[count]
                    profit = max(take, skip)

                curr[count] = profit

            after = curr[:]

        return after[2 * k]
