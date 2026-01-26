# Matrix Chain Multiplication Problem using Dynamic Programming
class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def memoization(i, j, dp):

            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = float("inf")
            for k in range(i, j):
                steps = (
                    arr[i - 1] * arr[k] * arr[j]
                    + memoization(i, k, dp)
                    + memoization(k + 1, j, dp)
                )

                mini = min(mini, steps)
                dp[i][j] = mini
            return dp[i][j]

        return memoization(1, n - 1, dp)


class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n):
                mini = float("inf")
                for k in range(i, j):
                    steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]

                    mini = min(mini, steps)
                dp[i][j] = mini
        return dp[1][n - 1]


s = Solution()
print(s.matrixMultiplication([10, 20, 30]))  # Output: 6000
