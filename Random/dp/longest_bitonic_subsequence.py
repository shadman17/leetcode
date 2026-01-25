# Must solve longest increasing subsequence first
# Then solve longest increasing subsequence from the end
# Finally combine both results to get the longest bitonic subsequence

from typing import List


class Solution:
    def longestBitonicSequence(self, n: int, nums: List[int]) -> int:

        dp1 = [1] * n
        dp2 = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[j])

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if nums[j] < nums[i]:
                    dp2[i] = max(dp2[i], 1 + dp2[j])

        maxi = 0
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                maxi = max(maxi, (dp1[i] + dp2[i] - 1))

        return maxi
