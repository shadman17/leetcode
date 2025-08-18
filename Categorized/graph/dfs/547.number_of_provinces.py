from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, adjlist, vis):
            vis[i] = 1
            for neighbor in adjlist[i]:
                if vis[neighbor] == 0:
                    dfs(neighbor, adjlist, vis)

        n = len(isConnected)
        vis = [0] * n

        adjlist = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adjlist[i].append(j)
                    adjlist[j].append(i)

        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                cnt += 1
                dfs(i, adjlist, vis)

        return cnt


s = Solution()
print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
