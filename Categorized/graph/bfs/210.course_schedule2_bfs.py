class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        adjlist = {i: [] for i in range(numCourses)}
        result = list()
        q = deque()
        indegree = [0] * numCourses

        for src, des in prerequisites:
            adjlist[des].append(src)
            indegree[src] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            result.append(node)

            for nei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return result if len(result) == numCourses else []
