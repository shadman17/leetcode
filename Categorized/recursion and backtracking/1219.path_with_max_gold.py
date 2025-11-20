class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def backtrack(r, c, visited):
            if (
                r < 0
                or c < 0
                or r == m
                or c == n
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0

            total = grid[r][c]
            visited.add((r, c))

            total += max(
                backtrack(r + 1, c, visited),
                backtrack(r - 1, c, visited),
                backtrack(r, c + 1, visited),
                backtrack(r, c - 1, visited),
            )
            visited.remove((r, c))

            return total

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                answer = backtrack(i, j, set())
                result = max(result, answer)

        return result
