# class Solution:
#     def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
#         happiness.sort(reverse=True)
#         n = len(happiness)
#         total = 0
#         for i in range(k):
#             cur = happiness[i] - i
#             total += cur if cur > 0 else 0

#         return total

import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for h in happiness:
            heapq.heappush(heap, -h)
        total = 0

        for i in range(k):
            cur = -heapq.heappop(heap) - i
            total += cur if cur > 0 else 0
        return total
