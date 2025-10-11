class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != INF and dist[via][j]!= INF:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
                 
        answer = -1
        citycount = n

        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= citycount:
                citycount = count
                answer = i

        return answer