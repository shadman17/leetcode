class Solution:
    def lcsprint(self, text1: str, text2: str) -> str:
        m = len(text1)
        n = len(text2)

        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for ind1 in range(1, m + 1):
                for ind2 in range(1, n + 1):
                    if text1[ind1 - 1] == text2[ind2 - 1]:
                        dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

                    else:
                        dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

            return dp[m][n]

        length = longestCommonSubsequence(self, text1, text2)
        i = m, j = n
        index = length - 1
        res = [] * length
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                res[index] = text1[i - 1]
                index -= 1

            elif text1[i - 1] > text2[j - 1]:
                i -= 1
            else:
                j -= 1

        return "".join(res)


s = Solution()
print(s.lcsprint("abcde", "ace"))
