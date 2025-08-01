from typing import List

# class Solution:
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         i, j = 0, len(nums) - 1
#         length = len(nums)

#         while i < length and j > -1:
#             while i < length and j > -1 and nums[i] % 2 == 0:
#                 i += 2

#             while i < length and j > -1 and nums[j] % 2 == 1:
#                 j -= 2

#             if i < length and j > -1:
#                 nums[i], nums[j] = nums[j], nums[i]
#             i += 2
#             j -= 2

#         return nums


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        sz = len(nums)

        while i < sz and j < sz:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2

        return nums


s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))
print(s.sortArrayByParityII([2, 3]))
