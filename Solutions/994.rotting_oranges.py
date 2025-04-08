from typing import List
from collections import deque

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
    
    
s = Solution()
print(s.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting(grid = [[0, 2]]))
print(s.orangesRotting(grid = [[0, 1]]))