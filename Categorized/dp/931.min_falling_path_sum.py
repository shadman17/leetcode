# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         def memoization(i, j, dp):
#             if j < 0 or j == n:
#                 return float("inf")
#             if i == 0:
#                 return matrix[0][j]

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             left = matrix[i][j] + memoization(i - 1, j - 1, dp)
#             right = matrix[i][j] + memoization(i - 1, j + 1, dp)
#             up = matrix[i][j] + memoization(i - 1, j, dp)

#             dp[i][j] = min(left, right, up)
#             return dp[i][j]

#         mini = float('inf')
#         dp = [[-1]* n for _ in range(n)]
#         for i in range(n):
#             mini = min(mini, memoization(n-1, i, dp))

#         return mini


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):

                left = matrix[i][j] + dp[i - 1][j - 1] if j > 0 else float("inf")
                right = matrix[i][j] + dp[i - 1][j + 1] if j < n - 1 else float("inf")
                up = matrix[i][j] + dp[i - 1][j]
                dp[i][j] = min(left, right, up)

        mini = float("inf")
        for j in range(n):
            mini = min(mini, dp[n - 1][j])

        return mini


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[0][:]

        for i in range(1, n):
            cur = [0] * n
            for j in range(n):
                left = prev[j - 1] if j > 0 else float("inf")
                up = prev[j]
                right = prev[j + 1] if j < n - 1 else float("inf")
                cur[j] = matrix[i][j] + min(left, up, right)
            prev = cur[:]

        mini = float("inf")
        for j in range(n):
            mini = min(mini, prev[j])

        return mini
