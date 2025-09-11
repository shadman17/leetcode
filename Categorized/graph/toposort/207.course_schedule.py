# Cycle detection acyclic graph


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [0] * numCourses
        path_visited = [0] * numCourses

        adjlist = {i: [] for i in range(numCourses)}

        for src, des in prerequisites:
            adjlist[src].append(des)

        def dfs(node):
            visited[node] = 1
            path_visited[node] = 1
            for nei in adjlist[node]:
                if visited[nei] == 1 and path_visited[nei] == 1:
                    return True
                elif visited[nei] == 0:
                    if dfs(nei) == True:
                        return True

            path_visited[node] = 0
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i) == True:
                    return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        # define visited
        visited = set()

        # define dfs
        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs] == []:
                return True

            visited.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            adjList[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
