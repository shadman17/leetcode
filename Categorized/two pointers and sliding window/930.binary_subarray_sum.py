class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(goal):
            if goal < 0:
                return 0

            l, r, count, total = 0, 0, 0, 0
            n = len(nums)
            while r < n:
                total += nums[r]

                while total > goal:
                    total -= nums[l]
                    l += 1

                count += r - l + 1

                r += 1

            return count

        return helper(goal) - helper(goal - 1)
