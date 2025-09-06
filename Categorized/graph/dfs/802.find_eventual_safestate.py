class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        total_node = len(graph)
        visited = [0] * total_node
        path_visited = [0] * total_node
        check = [0] * total_node

        def dfs(node, adjlist):
            visited[node] = 1
            path_visited[node] = 1
            check[node] = 0

            for nei in adjlist[node]:
                if visited[nei] == 0:
                    if dfs(nei, adjlist) == True:
                        return True

                elif visited[nei] == 1 and path_visited[nei] == 1:
                    return True

            path_visited[node] = 0
            check[node] = 1
            return False

        adjlist = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for val in graph[i]:
                adjlist[i].append(val)

        for i in range(len(graph)):
            if not visited[i]:
                dfs(i, adjlist)

        answer = []
        for i in range(len(graph)):
            if check[i] == 1:
                answer.append(i)
        return answer
