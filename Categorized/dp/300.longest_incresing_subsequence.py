# TLE for memoization
from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)

#         def memoization(ind, prev_ind, dp):
#             if ind == n:
#                 return 0

#             if dp[ind][prev_ind + 1] != -1:
#                 return dp[ind][prev_ind + 1]

#             not_take = memoization(ind + 1, prev_ind, dp)
#             take = float("-inf")
#             if prev_ind == -1 or nums[prev_ind] < nums[ind]:
#                 take = 1 + memoization(ind + 1, ind, dp)

#             dp[ind][prev_ind + 1] = max(take, not_take)
#             return dp[ind][prev_ind + 1]

#         return memoization(0, -1, [[-1] * (n + 1) for _ in range(n)])


# tabulation
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                not_take = dp[ind + 1][prev_ind + 1]
                take = float("-inf")
                if prev_ind == -1 or nums[prev_ind] < nums[ind]:
                    take = 1 + dp[ind + 1][ind + 1]

                dp[ind][prev_ind + 1] = max(take, not_take)

        return dp[0][0]


# space optimization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        after = [0] * (n + 1)
        cur = [0] * (n + 1)

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                not_take = after[prev_ind + 1]
                take = float("-inf")
                if prev_ind == -1 or nums[prev_ind] < nums[ind]:
                    take = 1 + after[ind + 1]

                cur[prev_ind + 1] = max(take, not_take)

            after = cur[:]

        return after[0]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

            maxi = max(maxi, dp[i])

        return maxi


s = Solution()
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
