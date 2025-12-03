from collections import deque


class Solution:
    def findOrder(words):
        q = deque()
        nodes = set([ch for word in words for ch in word])

        adjlist = {}
        indegree = {}
        for node in nodes:
            adjlist[node] = set()
            indegree[node] = 0

        for i in range(len(words) - 1):
            s1 = words[i]
            s2 = words[i + 1]
            if len(s1) > len(s2) and s1.startswith(s2):
                return ""
            minlen = min(len(s1), len(s2))

            for j in range(minlen):
                if s1[j] != s2[j]:
                    if s2[j] not in adjlist[s1[j]]:
                        adjlist[s1[j]].add(s2[j])
                        indegree[s2[j]] += 1
                    break

        for key in indegree.keys():
            if indegree[key] == 0:
                q.append(key)

        result = []
        while q:
            node = q.popleft()
            result.append(node)

            for nei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(result) if len(result) == len(nodes) else ""
