import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = nums[:]
        min_heap = list(tuple((value, index) for index, value in enumerate(nums)))

        heapq.heapify(min_heap)
        for _ in range(k):
            min_value, i = heapq.heappop(min_heap)
            result[i] *= multiplier
            heapq.heappush(min_heap, (result[i], i))
        return result


s = Solution()
print(s.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
# print(s.getFinalState(nums=[1, 2], k=3, multiplier=4))
