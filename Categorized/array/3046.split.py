from collections import Counter
from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False

        counter = Counter(nums)

        for freq in counter.values():
            if freq > 2:
                return False

        return True
    
s = Solution()
print(s.isPossibleToSplit(nums = [1,1,2,2,3,4]))
print(s.isPossibleToSplit(nums = [1,1,1,1]))
            