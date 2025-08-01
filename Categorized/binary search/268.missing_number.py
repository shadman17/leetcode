from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == mid:
                left = mid + 1

            else:
                right = mid

        return left


s = Solution()
print(s.missingNumber([0, 3, 5, 8, 4, 6, 1, 9, 7]))
