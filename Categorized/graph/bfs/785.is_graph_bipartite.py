class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        queue = deque()

        def bfs(i):
            queue.append(i)
            color[i] = 1
            while queue:
                x = queue.popleft()
                for nei in graph[x]:
                    if color[x] == color[nei]:
                        return False

                    elif color[nei] == 0:
                        queue.append(nei)
                        color[nei] = -1 * color[x]

            return True

        for i in range(len(graph)):
            if color[i] == 0:
                if bfs(i) == False:
                    return False

        return True
