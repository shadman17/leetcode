from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        countZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for k in range(j, len(nums)):
            nums[j] = 0
            j += 1

    # Two pointer
    # def moveZeroes(self, nums: List[int]) -> None:
    #     left = 0

    #     for right in range(len(nums)):
    #         if nums[right] != 0:
    #             nums[right], nums[left] = nums[left], nums[right]
    #             left += 1


s = Solution()
print(s.moveZeroes(nums=[0, 1, 0, 3, 12]))
print(s.moveZeroes(nums=[0]))
