from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, maxlen, zeroes = 0, 0, 0, 0
        print(zeroes)
        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen


s = Solution()
# print(s.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(s.longestOnes(nums=[0, 0, 0, 1], k=4))
