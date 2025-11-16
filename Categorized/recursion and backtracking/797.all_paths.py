class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def dfs(node, arr):
            if node == n-1:
                res.append(arr[:])
                return
            
            for i in range(len(graph[node])):
                arr.append(graph[node][i])
                dfs(graph[node][i], arr)
                arr.pop()

        dfs(0, [0])
        return res