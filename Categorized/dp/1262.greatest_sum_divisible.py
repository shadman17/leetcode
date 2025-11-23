class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        dp = [[-1] * 3 for _ in range(len(nums) + 1)]

        def backtrack(ind, remainder, dp):
            if ind == len(nums):
                if remainder == 0:
                    return 0
                return float("-inf")

            if dp[ind][remainder] != -1:
                return dp[ind][remainder]

            pick = nums[ind] + backtrack(ind + 1, (remainder + nums[ind]) % 3, dp)
            not_pick = backtrack(ind + 1, (remainder % 3), dp)

            dp[ind][remainder] = max(pick, not_pick)
            return dp[ind][remainder]

        return backtrack(0, 0, dp)
