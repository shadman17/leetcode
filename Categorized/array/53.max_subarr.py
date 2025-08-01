# Kadane's Algorithm

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0

        for i in range(len(nums)):

            curSum += nums[i]
            if maxSum < curSum:
                maxSum = curSum  # maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0  # curSum = max(curSum, 0)

        return maxSum
