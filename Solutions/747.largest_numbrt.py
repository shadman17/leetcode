from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        if sorted_nums[-2] * 2 <= sorted_nums[-1]:
            return nums.index(sorted_nums[-1])

        return -1


# class Solution:
#     def dominantIndex(self, nums: List[int]) -> int:
#         sort = sorted(enumerate(nums), key=lambda x: x[1])
#         print(sort)
#         for i in range(len(nums) - 1):
#             if sort[i][1] > sort[-1][1] // 2:
#                 return -1
#         return sort[-1][0]


s = Solution()
print(s.dominantIndex([3, 6, 1, 0]))
print(s.dominantIndex([1, 2, 3, 4]))
print(s.dominantIndex([2, 3, 6]))
