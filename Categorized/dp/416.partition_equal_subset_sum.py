# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         def memoization(ind, cur, dp):
#             if cur == 0:
#                 return True

#             if ind == 0:
#                 return nums[0] == cur

#             if cur < 0:
#                 return False

#             if dp[ind][cur] != -1:
#                 return dp[ind][cur]

#             notpick = memoization(ind - 1, cur, dp)
#             pick = False
#             if nums[ind] <= cur:
#                 pick = memoization(ind - 1, cur - nums[ind], dp)

#             dp[ind][cur] = notpick or pick
#             return dp[ind][cur]

#         total = sum(nums)

#         if total % 2 == 1:
#             return False
#         n = len(nums)
#         total = total // 2

#         return memoization(n - 1, total, [[-1] * (total + 1) for _ in range(n)])


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        n = len(nums)
        total = total // 2

        dp = [[False] * (total + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= total:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, total + 1):
                not_take = dp[i - 1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]
                dp[i][j] = not_take or take

        return dp[n - 1][total]
