import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        adjlist = {i: [] for i in range(n)}
        mod = 10**9 + 7
        for src, des, time in roads:
            adjlist[src].append((des, time))
            adjlist[des].append((src, time))

        minHeap = []
        heapq.heappush(minHeap, (0, 0))
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if t > dist[node]:
                continue
            for nei, t2 in adjlist[node]:
                if t + t2 < dist[nei]:
                    dist[nei] = t + t2
                    heapq.heappush(minHeap, (t + t2, nei))
                    ways[nei] = ways[node]

                elif t + t2 == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % mod

        return ways[n - 1] % mod
