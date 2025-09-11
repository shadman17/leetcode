from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = [0] * len(graph)
        q = deque()
        adjlist = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for j in graph[i]:
                adjlist[j].append(i)
                indegree[i] += 1

        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for nei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        result.sort()
        return result


s = Solution()
print(s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
