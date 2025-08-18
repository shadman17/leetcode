class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c, arr):

            if r < 0 or c < 0 or r == m or c == n or arr[r][c] == "0":
                return 0

            arr[r][c] = "0"

            dfs(r + 1, c, arr)
            dfs(r - 1, c, arr)
            dfs(r, c + 1, arr)
            dfs(r, c - 1, arr)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, grid)

        return count
