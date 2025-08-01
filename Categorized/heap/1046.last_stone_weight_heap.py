import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)
        return -stones[0] if len(stones) == 1 else 0


s = Solution()
print(s.lastStoneWeight([4, 3, 2, 3, 4]))
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeight([2, 2]))
