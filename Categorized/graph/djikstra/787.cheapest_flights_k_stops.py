class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        INF = float("inf")
        dist = [INF] * n
        dist[src] = 0

        adjlist = {i: [] for i in range(n)}

        for a, b, cost in flights:
            adjlist[a].append((b, cost))

        q = deque()
        q.append((0, src, 0))

        while q:
            stop, node, cost = q.popleft()
            if stop > k:
                continue
            for nei, cost2 in adjlist[node]:
                if cost + cost2 < dist[nei] and stop <= k:
                    dist[nei] = cost + cost2
                    q.append((stop + 1, nei, cost + cost2))

        if dist[dst] == INF:
            return -1

        return dist[dst]
