# User function Template for python3
from collections import defaultdict, deque
from typing import List


class Solution:

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:

        adjlist = {i: [] for i in range(V)}
        indegree = [0] * V
        q = deque()
        for u, v, w in edges:
            adjlist[u].append((v, w))
            indegree[v] += 1

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei, wei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        INF = float("inf")
        dist = [INF] * V
        dist[0] = 0

        for u in topo:

            for v, w in adjlist[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        result = []
        for d in dist:
            if d == INF:
                result.append(-1)
            else:
                result.append(d)

        return result
        # return [(-1 if d == INF else d) for d in dist]


# User function Template for python3
# from collections import defaultdict, deque
# from typing import List


# class Solution:

#     def shortestPath(self, V: int, E: int,
#                      edges: List[List[int]]) -> List[int]:

#         def dfs(src, adjlist, visit, topo):
#             if src in visit:
#                 return
#             visit.add(src)
#             for nei, w in adjlist[src]:
#                 dfs(nei, adjlist, visit, topo)

#             topo.append(src)


#         adjlist = {i: [] for i in range(V)}
#         for u, v, w in edges:
#             adjlist[u].append((v, w))

#         visited = set()
#         topo = []
#         for i in range(V):
#             if i not in visited:
#                 dfs(i, adjlist, visited, topo)

#         topo.reverse()

#         INF = float('inf')
#         dist = [INF] * V
#         dist[0] = 0

#         for u in topo:

#             for v, w in adjlist[u]:
#                 if dist[u] + w < dist[v]:
#                     dist[v] = dist[u] + w

#         result = []
#         for d in dist:
#             if d == INF:
#                 result.append(-1)
#             else:
#                 result.append(d)

#         return result
