from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)

        return len(nums) != len(x)


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4]))
