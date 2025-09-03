class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = [0] * len(graph)

        def dfs(i, color):
            visit[i] = color
            for nei in graph[i]:
                if visit[nei] == 0:
                    if dfs(nei, -color) == False:
                        return False
                elif visit[nei] == color:
                    return False
            return True

        for i in range(len(graph)):
            if visit[i] == 0:
                if dfs(i, 1) == False:
                    return False

        return True
