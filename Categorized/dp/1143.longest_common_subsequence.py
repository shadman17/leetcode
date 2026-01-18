# Leetcode Problem: 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Memoization Approach
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m = len(text1)
#         n = len(text2)

#         def memoization(ind1, ind2, dp):
#             if ind1 < 0 or ind2 < 0:
#                 return 0

#             if dp[ind1][ind2] != -1:
#                 return dp[ind1][ind2]

#             if text1[ind1] == text2[ind2]:
#                 dp[ind1][ind2] = 1 + memoization(ind1 - 1, ind2 - 1, dp)

#             else:
#                 dp[ind1][ind2] = max(
#                     memoization(ind1, ind2 - 1, dp), memoization(ind1 - 1, ind2, dp)
#                 )

#             return dp[ind1][ind2]

#         return memoization(m - 1, n - 1, [[-1] * n for _ in range(m)])


# Tabulation Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for ind1 in range(1, m + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[m][n]


# Space Optimized Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for ind1 in range(1, m + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]

                else:
                    curr[ind2] = max(prev[ind2], curr[ind2 - 1])
            prev = curr[:]

        return prev[n]
