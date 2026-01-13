# Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def recursion(ind):
            if ind == 0:
                return nums[ind]

            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind] + recursion(ind - 2)
            not_pick = recursion(ind - 1)

            dp[ind] = max(pick, not_pick)

            return dp[ind]

        return recursion(n - 1)


# Tabulation


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        dp[0] = nums[0]

        for ind in range(1, n):
            pick = nums[ind]
            if ind > 1:
                pick += dp[ind - 2]
            not_pick = dp[ind - 1]

            dp[ind] = max(pick, not_pick)

        return dp[n - 1]


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         if len(nums) == 1:
#             return nums[0]

#         dp = [0] * (len(nums))
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             left = nums[i] + dp[i - 2]
#             right = dp[i - 1]
#             dp[i] = max(left, right)

#         return dp[-1]


# Space Optimized DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        prev2 = 0
        prev = nums[0]

        for ind in range(1, n):
            pick = nums[ind]
            if ind > 1:
                pick += prev2
            not_pick = prev

            cur = max(pick, not_pick)
            prev2 = prev
            prev = cur

        return prev


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         if len(nums) == 1:
#             return nums[0]

#         prev2 = nums[0]
#         prev = max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             left = nums[i] + prev2
#             right = prev
#             cur = max(left, right)
#             prev2 = prev
#             prev = cur

#         return prev
