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
