class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        def bfs(grid):
            queue = deque()
            visit = set()
            queue.append((0, 0))
            visit.add((0, 0))

            length = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r == rows - 1 and c == cols - 1:
                        return length

                    neighbors = [
                        [0, 1],
                        [0, -1],
                        [1, 0],
                        [-1, 0],
                        [1, 1],
                        [1, -1],
                        [-1, 1],
                        [-1, -1],
                    ]
                    for dr, dc in neighbors:
                        if (
                            0 <= r + dr < rows
                            and 0 <= c + dc < cols
                            and (r + dr, c + dc) not in visit
                            and grid[r + dr][c + dc] != 1
                        ):
                            queue.append((r + dr, c + dc))
                            visit.add((r + dr, c + dc))
                length += 1

            return -1

        return bfs(grid)


# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
#             return -1

#         queue = deque()
#         visit = [[0] * COLS for i in range(ROWS)]
#         length = 1
#         queue.append((0, 0))
#         visit[0][0] = 1

#         while queue:
#             for i in range(len(queue)):
#                 r, c = queue.popleft()
#                 if r == ROWS - 1 and c == COLS - 1:
#                     return length

#                 directions = [
#                     [0, 1],
#                     [1, 0],
#                     [0, -1],
#                     [-1, 0],
#                     [-1, -1],
#                     [-1, 1],
#                     [1, -1],
#                     [1, 1],
#                 ]
#                 for dr, dc in directions:
#                     nr, nc = r + dr, c + dc

#                     if (
#                         0 <= nr < ROWS
#                         and 0 <= nc < COLS
#                         and visit[nr][nc] != 1
#                         and grid[nr][nc] == 0
#                     ):
#                         queue.append((nr, nc))
#                         visit[nr][nc] = 1
#             length += 1

#         return -1
