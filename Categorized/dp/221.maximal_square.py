from typing import List


# Memoization approach
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def memoization(i, j, dp):
            if i == m or j == n or matrix[i][j] == "0":
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            right = memoization(i, j + 1, dp)
            bottom = memoization(i + 1, j, dp)
            diag = memoization(i + 1, j + 1, dp)

            dp[i][j] = 1 + min(right, bottom, diag)
            return dp[i][j]

        dp = [[-1] * (n) for _ in range(m)]
        maxi = 0
        for i in range(m):
            for j in range(n):
                maxi = max(maxi, memoization(i, j, dp))

        return maxi * maxi


# Tabulation approach
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right = dp[i][j + 1]
                    bottom = dp[i + 1][j]
                    diag = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(right, bottom, diag)

        maxi = 0
        for i in range(m):
            for j in range(n):
                maxi = max(maxi, dp[i][j])

        return maxi * maxi


s = Solution()
print(
    s.maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)  # Output: 4
