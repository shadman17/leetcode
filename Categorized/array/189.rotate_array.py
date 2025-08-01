from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newarr = [0] * n
        k = k % n

        for i in range(n):
            newarr[(i + k) % n] = nums[i]

        nums[:] = newarr


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
