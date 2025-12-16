from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        rows, cols = m, n
        fresh = 0
        time = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1

                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                r, c = cur

                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1

# Not Modifying the input array
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         queue = deque()
#         m, n = len(grid), len(grid[0])

#         tm = 0
#         visited = [[0] * n for i in range(m)]

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 2:
#                     queue.append(((i, j), tm))
#                     visited[i][j] == 2

#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#         while queue:
#             coordinates, tm = queue.popleft()
#             x, y = coordinates

#             for dx, dy in directions:
#                 nx = x + dx
#                 ny = y + dy

#                 if (
#                     0 <= nx < m
#                     and 0 <= ny < n
#                     and visited[nx][ny] != 2
#                     and grid[nx][ny] == 1
#                 ):
#                     queue.append(((nx, ny), tm + 1))
#                     visited[nx][ny] = 2

#         for i in range(m):
#             for j in range(n):
#                 if visited[i][j] == 0 and grid[i][j] == 1:
#                     return -1

#         return tm

s = Solution()
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting(grid=[[0, 2]]))
print(s.orangesRotting(grid=[[0, 1]]))
