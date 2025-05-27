from collections import defaultdict
import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        adj = defaultdict(list)

        for i in range(length):
            x1, y1 = points[i]
            for j in range(i+1, length):
                x2, y2 = points[j]
                val = abs(x1-x2) + abs(y1-y2)
                adj[i].append((val, j))
                adj[j].append((val, i))
        
        res = 0
        visited = set()
        minHeap = [(0,0)]

        while minHeap:
            cost, i = heapq.heappop(minHeap)

            if i in visited:
                continue

            res += cost
            visited.add(i)

            for cost, neighbour in adj[i]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (cost, neighbour))

        return res 

s = Solution()
print(s.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
