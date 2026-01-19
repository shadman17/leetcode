class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        def lcs(s1, s2, dp, m, n):
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        lcs_table = lcs(str1, str2, dp, m, n)

        i = m
        j = n
        res = ""

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res += str1[i - 1]
                i -= 1
                j -= 1

            elif dp[i - 1][j] > dp[i][j - 1]:
                res += str1[i - 1]
                i -= 1
            else:
                res += str2[j - 1]
                j -= 1

        while i > 0:
            res += str1[i - 1]
            i -= 1

        while j > 0:
            res += str2[j - 1]
            j -= 1

        res = res[::-1]
        return res
