import heapq


class Solution:
    def dijkstra(self, V, edges, src):
        # code here
        adjlist = {i: [] for i in range(V)}
        for u, v, w in edges:
            adjlist[u].append((v, w))
            adjlist[v].append((u, w))

        INF = float("inf")
        dist = [INF] * V
        dist[src] = 0
        minHeap = []
        heapq.heappush(minHeap, (0, src))

        while minHeap:
            dist_u, u = heapq.heappop(minHeap)  # distance so far to u
            if dist_u > dist[u]:
                continue

            for v, weight in adjlist[u]:  # edge weight
                if dist_u + weight < dist[v]:
                    dist[v] = dist_u + weight
                    heapq.heappush(minHeap, (dist[v], v))

        return dist
