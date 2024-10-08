from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if nums[mid + 1] == target:
                    return [mid, mid + 1]
                elif nums[mid - 1] == target:
                    return [mid - 1, mid]
                else:
                    return [mid, mid]

            elif nums[mid] <= target:
                left = mid + 1

            else:
                right = mid - 1

        return [-1, -1]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 9, 10], 8))
