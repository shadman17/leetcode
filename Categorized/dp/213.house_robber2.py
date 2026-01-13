"""
1. Must solve house robber (Leetcode 198)
2The intuition is that I can't take both first and last element.
Hence, I try to identify the maximum one while taking first element or last element
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
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

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(helper(nums[1:n]), helper(nums[: n - 1]))
