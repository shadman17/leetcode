from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i in [0, m - 1] or j in [0, n - 1]):
                    queue.append((i, j))
                    visited[i][j] = 1

        while queue:
            x, y = queue.popleft()

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and grid[nx][ny] == 1
                    and visited[nx][ny] == 0
                ):
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    count += 1

        return count


s = Solution()
print(s.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
