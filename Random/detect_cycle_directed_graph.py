from collections import defaultdict


class Solution:
    def isCycle(self, V, edges):

        visited = [0] * V
        path_visited = [0] * V
        adjlist = defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)

        def dfs(i):
            visited[i] = 1
            path_visited[i] = 1

            for nei in adjlist[i]:
                if not visited[nei]:
                    if dfs(nei) == True:
                        return True

                elif path_visited[nei] == 1:
                    return True

            path_visited[i] = 0
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i) == True:
                    return True

        return False
