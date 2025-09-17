# User function Template for python3
import heapq
from typing import List


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adjlist = {i: [] for i in range(1, n + 1)}

        for src, des, weight in edges:
            adjlist[src].append((des, weight))
            adjlist[des].append((src, weight))

        INF = float("inf")
        dist = [INF] * (n + 1)
        parent = [i for i in range(n + 1)]

        minHeap = []
        dist[1] = 0
        heapq.heappush(minHeap, (0, 1))

        while minHeap:
            dist_u, u = heapq.heappop(minHeap)

            if dist_u > dist[u]:
                continue

            for v, w in adjlist[u]:
                if dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    parent[v] = u
                    heapq.heappush(minHeap, (dist[v], v))

        if dist[n] == INF:
            return [-1]
        path = []
        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        return [dist[n]] + path
