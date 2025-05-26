from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        shortest = {}
        minHeap = [(0, k)]

        for u, v, w in times:
            adj[u].append((w, v))

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            if v1 in shortest:
                continue

            shortest[v1] = w1

            for w2, v2 in adj[v1]:
                if v2 not in shortest:
                    heapq.heappush(minHeap, (w1+w2, v2))

        if len(shortest) == n:
            return max(shortest.values())
        return -1 