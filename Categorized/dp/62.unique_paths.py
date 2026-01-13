class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def memoization(r, c, rows, cols, cache):
        #     if r < 0 or c < 0:
        #         return 0

        #     if r == 0 and c == 0:
        #         return 1

        #     if cache[r][c] != -1:
        #         return cache[r][c]

        #     right = memoization(r - 1, c, rows, cols, cache)
        #     down = memoization(r, c - 1, rows, cols, cache)

        #     cache[r][c] = right + down
        #     return cache[r][c]

        # return memoization(m - 1, n - 1, m, n, [[-1] * n for i in range(m)])

        # def tabulation(m: int, n: int) -> int:
        #     dp = [[0] * n for _ in range(m)]

        #     for i in range(m):
        #         for j in range(n):
        #             if i == 0 and j == 0:
        #                 dp[0][0] = 1

        #             else:
        #                 up = dp[i - 1][j] if i > 0 else 0
        #                 left = dp[i][j - 1] if j > 0 else 0

        #                 dp[i][j] = up + left

        #     return dp[m - 1][n - 1]

        # return tabulation(m, n)

        # def space_optimized_dp(m: int, n: int) -> int:
        #     prevrow = [0] * n

        #     for i in range(m):
        #         for j in range(n):
        #             if i == 0 and j == 0:
        #                 prevrow[0] = 1

        #             else:
        #                 up = prevrow[j] if i > 0 else 0
        #                 left = prevrow[j - 1] if j > 0 else 0

        #                 prevrow[j] = up + left

        #     return prevrow[n - 1]

        # return space_optimized_dp(m, n)

        def space_optimized_dp(m: int, n: int) -> int:
            prevrow = [0] * n

            for i in range(m):
                cur = [0] * n
                for j in range(n):
                    if i == 0 and j == 0:
                        cur[j] = 1

                    else:
                        up = prevrow[j] if i > 0 else 0
                        left = cur[j - 1] if j > 0 else 0
                        cur[j] = up + left
                prevrow = cur
            return prevrow[n - 1]

        return space_optimized_dp(m, n)


s = Solution()
print(s.uniquePaths(3, 7))
