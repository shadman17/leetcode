# Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)

        def func(ind):
            if ind == 0:
                return nums[ind]

            if dp[ind] != -1:
                return dp[ind]

            if ind < 0:
                return 0

            left = nums[ind] + func(ind - 2)
            right = func(ind - 1)

            dp[ind] = max(left, right)
            return dp[ind]

        return func(len(nums) - 1)


# DP Bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            left = nums[i] + dp[i - 2]
            right = dp[i - 1]
            dp[i] = max(left, right)

        return dp[-1]


# Space Optimized DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            left = nums[i] + prev2
            right = prev
            cur = max(left, right)
            prev2 = prev
            prev = cur

        return prev
