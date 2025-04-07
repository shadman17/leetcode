import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heap.append([dist, point[0], point[1]])

        # for x, y in points:
        #     dist = x **2 + y**2
        #     heap.append([dist, x, y])

        heapq.heapify(heap)
        res = []
        # while k > 0:
        #     x = heapq.heappop(heap)
        #     res.append([x[1], x[2]])
        #     k -= 1

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1

        return res


s = Solution()
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
