from typing import List
import math
import heapq

# TC - O(log n)
class Solution:
    def powerFunc(self, x, n):
        m = n
        if n < 0:
            n = -n
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
                n -= 1
            else:
                n = n // 2
                x = x * x
        if m < 0:
            ans = 1/ans
        return ans
    
s = Solution()
print(s.powerFunc(2, -4))