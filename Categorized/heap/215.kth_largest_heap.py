import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


s = Solution()
print(s.findKthLargest([1, 2, 4, 3, 5, 6], 2))
