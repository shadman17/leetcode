from typing import List


class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     result = prices.copy()
    #     length = len(prices)
    #     for i in range(length):
    #         j = i + 1
    #         while j < length:
    #             if prices[j] <= prices[i]:
    #                 result[i] = prices[i] - prices[j]
    #                 break
    #             j += 1

    #     return result
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]

            stack.append(i)
        return prices


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
print(s.finalPrices([1, 2, 3, 4, 5]))
print(s.finalPrices([10, 1, 1, 6]))
print(s.finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
