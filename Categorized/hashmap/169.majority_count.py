from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        return count.most_common()[0][0]

s = Solution()
print(s.majorityElement([3,2,3]))