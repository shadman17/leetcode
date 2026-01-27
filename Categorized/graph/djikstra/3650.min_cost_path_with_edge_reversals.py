from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i: [] for i in range(n)}
        for u, v, w in edges:
            adjlist[u].append((v, w))
            adjlist[v].append((u, 2 * w))

        INF = float("inf")
        dist = [INF] * n
        dist[0] = 0
        minHeap = []
        heapq.heappush(minHeap, (0, 0))

        while minHeap:
            w, u = heapq.heappop(minHeap)
            if w > dist[u]:
                continue
            for v, w in adjlist[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(minHeap, (dist[v], v))

        return dist[n - 1] if dist[n - 1] != INF else -1
