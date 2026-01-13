from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # def memoization(r, c, dp):
        #     if r < 0 or c < 0:
        #         return float("inf")

        #     if r == 0 and c == 0:
        #         return grid[0][0]

        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     left = grid[r][c] + memoization(r - 1, c, dp)
        #     up = grid[r][c] + memoization(r, c - 1, dp)

        #     dp[r][c] = min(left, up)
        #     return dp[r][c]

        # return memoization(m - 1, n - 1, [[-1] * n for _ in range(m)])

        # def tabulation(m, n):
        #     dp = [[0] * n for _ in range(m)]

        #     for i in range(m):
        #         for j in range(n):
        #             if i == 0 and j == 0:
        #                 dp[0][0] = grid[0][0]
        #             else:
        #                 left = grid[i][j] + dp[i - 1][j] if i > 0 else float("inf")
        #                 up = grid[i][j] + dp[i][j - 1] if j > 0 else float("inf")
        #                 dp[i][j] = min(left, up)
        #     return dp[m - 1][n - 1]

        # return tabulation(m, n)

        def space_optimized_dp(m, n):
            prevrow = [0] * n

            for i in range(m):
                cur = [0] * n
                for j in range(n):
                    if i == 0 and j == 0:
                        cur[j] = grid[0][0]
                    else:
                        left = grid[i][j] + prevrow[j] if i > 0 else float("inf")
                        up = grid[i][j] + cur[j - 1] if j > 0 else float("inf")
                        cur[j] = min(left, up)
                prevrow = cur
            return prevrow[n - 1]

        return space_optimized_dp(m, n)
