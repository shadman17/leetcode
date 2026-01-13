from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # def memoization(i, j, n, dp):
        #     if i == n - 1:
        #         return triangle[i][j]

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     down = triangle[i][j] + memoization(i + 1, j, n, dp)
        #     diagonal = triangle[i][j] + memoization(i + 1, j + 1, n, dp)

        #     dp[i][j] = min(down, diagonal)
        #     return dp[i][j]

        # return memoization(0, 0, n, [[-1] * n for _ in range(n)])

        # def tabulation(dp):
        #     for i in range(n):
        #         dp[n - 1][i] = triangle[n - 1][j]

        #     for i in range(n - 2, -1, -1):
        #         for j in range(i, -1, -1):
        #             down = triangle[i][j] + dp[i + 1][j]
        #             diagonal = triangle[i][j] + dp[i + 1][j + 1]
        #             dp[i][j] = min(down, diagonal)

        #     return dp[0][0]

        # return tabulation([[-1] * n for _ in range(n)])

        def space_optimized_dp():
            nextone = [0] * n

            for j in range(n):
                nextone[j] = triangle[n - 1][j]

            for i in range(n - 2, -1, -1):
                cur = [0] * n
                for j in range(i, -1, -1):
                    down = triangle[i][j] + nextone[j]
                    diagonal = triangle[i][j] + nextone[j + 1]
                    cur[j] = min(down, diagonal)
                nextone = cur[:]

            return nextone[0]

        return space_optimized_dp()

        # def space_optimized_dp2():
        #     cur = [0] * n

        #     for j in range(n):
        #         cur[j] = triangle[n - 1][j]

        #     for i in range(n - 2, -1, -1):
        #         for j in range(i + 1):
        #             cur[j] = triangle[i][j] + min(cur[j], cur[j + 1])

        #     return cur[0]

        # return space_optimized_dp2()


s = Solution()
print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
