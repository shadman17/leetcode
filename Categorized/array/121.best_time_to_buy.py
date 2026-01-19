from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float("inf")

        for price in prices:
            if price < minprice:
                minprice = price

            elif price - minprice > maxprofit:
                maxprofit = price - minprice

        return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i] - mini  # potential profit if sold today
            profit = max(profit, cost)  # update max profit
            mini = min(
                mini, prices[i]
            )  # update minimum price so far, so the profit can be maximized in next iterations

        return profit


s = Solution()
print(s.maxProfit([7, 6, 5, 4]))
