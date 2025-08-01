from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float('inf')

        for price in prices:
            if price < minprice:
                minprice = price
             
            elif price - minprice > maxprofit:
                maxprofit = price - minprice

        return maxprofit
    
s = Solution()
print(s.maxProfit([7, 6, 5, 4]))
