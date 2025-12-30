from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            total ^= num

        return total


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
