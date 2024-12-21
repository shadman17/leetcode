from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        my_set = set(nums)
        my_list = sorted(my_set, reverse=True)
        return my_list[0] if len(my_list) in [1, 2] else my_list[2]


s = Solution()
print(s.thirdMax([1, 2, 3]))
print(s.thirdMax([1, 2]))
# print(s.thirdMax([1, 2, 3, 78, 9, 45, 7]))
print(s.thirdMax([2, 2, 3, 1]))
