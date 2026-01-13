class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # def memoization(r, c, cache):
        #     if r < 0 or c < 0 or obstacleGrid[r][c]:
        #         return 0

        #     if r == 0 and c == 0:
        #         return 1

        #     if cache[r][c] != -1:
        #         return cache[r][c]

        #     right = memoization(r - 1, c, cache)
        #     down = memoization(r, c - 1, cache)

        #     cache[r][c] = right + down
        #     return cache[r][c]

        # return memoization(
        #     len(obstacleGrid) - 1,
        #     len(obstacleGrid[0]) - 1,
        #     [[-1] * (len(obstacleGrid[0])) for i in range(len(obstacleGrid))],
        # )

        # def tabulation(m: int, n: int) -> int:
        #     dp = [[0] * n for _ in range(m)]

        #     for i in range(m):
        #         for j in range(n):
        #             if obstacleGrid[i][j]:
        #                 dp[i][j] = 0
        #             elif i == 0 and j == 0:
        #                 dp[0][0] = 1
        #             else:
        #                 up = dp[i - 1][j] if i > 0 else 0
        #                 left = dp[i][j - 1] if j > 0 else 0

        #                 dp[i][j] = up + left

        #     return dp[m - 1][n - 1]

        # return tabulation(len(obstacleGrid), len(obstacleGrid[0]))

        def space_optimized_dp(m: int, n: int) -> int:
            prev = [0] * n

            for i in range(m):
                cur = [0] * n
                for j in range(n):
                    if obstacleGrid[i][j]:
                        cur[j] = 0
                    elif i == 0 and j == 0:
                        cur[j] = 1
                    else:
                        up = prev[j] if i > 0 else 0
                        left = cur[j - 1] if j > 0 else 0

                        cur[j] = up + left
                prev = cur
            return prev[n - 1]

        return space_optimized_dp(len(obstacleGrid), len(obstacleGrid[0]))
