class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur += 1
                count += cur
            else:
                cur = 0

        return count

            