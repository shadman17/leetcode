# This will get TLE cause of recursion depth


# Memoization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def memoization(i, j, dp):
            if j == 0:
                return 1
            if i == 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i - 1] == t[j - 1]:
                dp[i][j] = memoization(i - 1, j - 1, dp) + memoization(i - 1, j, dp)

            else:
                dp[i][j] = memoization(i - 1, j, dp)

            return dp[i][j]

        m = len(s)
        n = len(t)
        return memoization(m, n, [[-1] * (n + 1) for _ in range(m + 1)])


# Tabulation
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


# Space Optimization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)

        prev[0] = cur[0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = prev[j - 1] + prev[j]

                else:
                    cur[j] = prev[j]

            prev = cur[:]
        return prev[n]


# More Space Optimization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        prev = [0] * (n + 1)

        prev[0] = 1

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    prev[j] = prev[j - 1] + prev[j]

        return prev[n]


s = Solution()
print(s.numDistinct("babgbag", "bag"))  # 5
