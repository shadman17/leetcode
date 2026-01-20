# Memoization #TLE
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        def memoization(ind, buy, dp):

            if ind == len(prices):
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]

            profit = 0
            if buy:
                take = -prices[ind] + memoization(ind + 1, 0, dp)
                skip = memoization(ind + 1, 1, dp)
                profit = max(take, skip)
            else:
                take = prices[ind] - fee + memoization(ind + 1, 1, dp)
                skip = memoization(ind + 1, 0, dp)
                profit = max(take, skip)

            dp[ind][buy] = profit
            return dp[ind][buy]

        dp = [[-1] * 2 for _ in range(len(prices) + 1)]
        return memoization(0, 1, dp)


# Tabulation
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        n = len(prices)
        dp[n][0] = 0
        dp[n][1] = 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    take = -prices[ind] + dp[ind + 1][0]
                    skip = dp[ind + 1][1]
                    profit = max(take, skip)
                else:
                    take = prices[ind] - fee + dp[ind + 1][1]
                    skip = dp[ind + 1][0]
                    profit = max(take, skip)

                dp[ind][buy] = profit

        return dp[0][1]


# Space optimization
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        after = [0] * 2
        cur = [0] * 2

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    take = -prices[ind] + after[0]
                    skip = after[1]
                    profit = max(take, skip)
                else:
                    take = prices[ind] - fee + after[1]
                    skip = after[0]
                    profit = max(take, skip)

                cur[buy] = profit

            after = cur[:]
        return after[1]


# Space optimization more!
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        after = [0] * 2
        cur = [0] * 2

        for ind in range(n - 1, -1, -1):

            cur[1] = max(-prices[ind] + after[0], after[1])
            cur[0] = max(prices[ind] - fee + after[1], after[0])

            after = cur[:]
        return after[1]


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        after_buy, after_not_buy = 0, 0

        for ind in range(n - 1, -1, -1):

            cur_buy = max(-prices[ind] + after_not_buy, after_buy)
            cur_not_buy = max(prices[ind] - fee + after_buy, after_not_buy)

            after_buy, after_not_buy = cur_buy, cur_not_buy

        return after_buy
