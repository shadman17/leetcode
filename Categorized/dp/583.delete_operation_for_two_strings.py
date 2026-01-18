class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def lcs(s1, s2):
            m = len(s1)
            n = len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for ind1 in range(1, m + 1):
                for ind2 in range(1, n + 1):
                    if s1[ind1 - 1] == s2[ind2 - 1]:
                        dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

                    else:
                        dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

            return dp[m][n]

        val = lcs(word1, word2)
        return len(word1) + len(word2) - 2 * val
