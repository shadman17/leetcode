from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [-1] * n

        def memoization(i, dp):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            length = 0
            localmax = float("-inf")
            maxi = float("-inf")

            for j in range(i, min(n, i + k)):
                length += 1
                localmax = max(localmax, arr[j])
                summ = (length * localmax) + memoization(j + 1, dp)
                maxi = max(maxi, summ)
            dp[i] = maxi
            return dp[i]

        return memoization(0, dp)


# Tabulation approach
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            length = 0
            localmax = float("-inf")
            maxi = float("-inf")
            for j in range(i, min(n, i + k)):
                length += 1
                localmax = max(localmax, arr[j])
                summ = (length * localmax) + dp[j + 1]
                maxi = max(maxi, summ)
            dp[i] = maxi

        return dp[0]


s = Solution()
print(s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))  # Output: 84
