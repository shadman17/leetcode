from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, value in enumerate(nums):
            dic[value] = i

        for i, value in enumerate(nums):
            remainder = target - value
            if remainder in dic and dic[remainder] != i:
                return [i, dic[remainder]]

        return []
