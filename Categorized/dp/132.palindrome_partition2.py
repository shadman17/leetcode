class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def palindrome_check(s):
            return s == s[::-1]

        def memoization(i, dp):
            mini = float("inf")
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            for j in range(i, n):
                if palindrome_check(s[i : j + 1]):
                    count = 1 + memoization(j + 1, dp)
                    mini = min(mini, count)

            dp[i] = mini
            return dp[i]

        return memoization(0, [-1] * n) - 1


# Tabulation approach
class Solution:
    def minCut(self, s: str) -> int:

        def palindrome_check(s):
            return s == s[::-1]

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            mini = float("inf")
            for j in range(i, n):
                if palindrome_check(s[i : j + 1]):
                    count = 1 + dp[j + 1]
                    mini = min(mini, count)

            dp[i] = mini

        return dp[0] - 1


s = Solution()
print(s.minCut("aab"))  # Output: 1
