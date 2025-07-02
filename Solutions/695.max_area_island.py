from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r,c))
            area = 1

            area += dfs(r+1, c)
            area += dfs(r, c+1)
            area += dfs(r-1, c)
            area += dfs(r, c-1)

            return area

        max_area = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_area = max(max_area, dfs(r,c))

        return max_area

s = Solution()

print(s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))