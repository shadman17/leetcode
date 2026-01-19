class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def memoization(i, j, dp):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = memoization(i - 1, j - 1, dp)
            else:
                dp[i][j] = 1 + min(
                    memoization(i, j - 1, dp),
                    memoization(i - 1, j, dp),
                    memoization(i - 1, j - 1, dp),
                )

            return dp[i][j]

        m = len(word1)
        n = len(word2)
        return memoization(m - 1, n - 1, [[-1] * (n) for _ in range(m)])


# Tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                    )

        return dp[m][n]


# Space Optimized
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)

        for j in range(n + 1):
            prev[j] = j

        for i in range(1, m + 1):
            cur[0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(
                        cur[j - 1],
                        prev[j],
                        prev[j - 1],
                    )
            prev = cur[:]

        return prev[n]


s = Solution()
print(s.minDistance(word1="horse", word2="ros"))
