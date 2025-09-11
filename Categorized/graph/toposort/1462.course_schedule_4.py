class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adjlist = {i: set() for i in range(numCourses)}
        indegree = [0] * numCourses
        isprereq = {i: set() for i in range(numCourses)}

        q = deque()

        for src, des in prerequisites:
            adjlist[src].add(des)
            indegree[des] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in adjlist[node]:
                isprereq[nei].add(node)
                isprereq[nei].update(isprereq[node])
                print(isprereq)
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        result = []
        for u, v in queries:
            if u in isprereq[v]:
                result.append(True)
            else:
                result.append(False)

        return result
