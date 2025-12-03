# from collections import defaultdict


# class Solution:
#     def isCycle(self, V, edges):

#         visited = [0] * V
#         path_visited = [0] * V
#         adjlist = defaultdict(list)
#         for u, v in edges:
#             adjlist[u].append(v)

#         def dfs(i):
#             visited[i] = 1
#             path_visited[i] = 1

#             for nei in adjlist[i]:
#                 if not visited[nei]:
#                     if dfs(nei) == True:
#                         return True

#                 elif path_visited[nei] == 1:
#                     return True

#             path_visited[i] = 0
#             return False

#         for i in range(V):
#             if not visited[i]:
#                 if dfs(i) == True:
#                     return True

#         return False

from collections import deque


class Solution:
    def isCycle(self, V, edges):
        q = deque()
        indegree = [0] * V
        adjlist = {i: [] for i in range(V)}

        for src, des in edges:
            adjlist[des].append(src)
            indegree[src] += 1

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()

            count += 1

            for nei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return True if count == V else False


s = Solution()
print(s.isCycle(V=4, edges=[[0, 1], [1, 2], [2, 3], [3, 3]]))
