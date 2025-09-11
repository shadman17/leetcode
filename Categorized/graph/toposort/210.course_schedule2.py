class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses  # # 0 = unvisited, 1 = visiting, 2 = visited
        adjlist = {i: [] for i in range(numCourses)}
        result = list()

        for src, des in prerequisites:
            adjlist[src].append(des)

        def dfs(node):
            if visited[node] == 1:  # Cycle Detected
                return False

            if visited[node] == 2:  # Already Processed
                return True

            visited[node] = 1
            for nei in adjlist[node]:
                if visited[nei] == 1:
                    return False
                if visited[nei] == 0 and not dfs(nei):
                    return False

            visited[node] = 2
            result.append(node)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []

        return result
