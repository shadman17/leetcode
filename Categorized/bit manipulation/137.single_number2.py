from collections import Counter

from typing import List


# Using extra space
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hashmap = Counter(nums)

#         for i, key in enumerate(hashmap):
#             if hashmap[key] == 1:
#                 return key


# Using bit manipulation without extra space


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            count = 0
            for j in range(len(nums)):
                if nums[j] & (1 << i):  # Check if the ith bit is set
                    count += 1

            if count % 3 == 1:
                ans = ans | (1 << i)  # Set the ith bit in the answer

        if ans >= (1 << 31):
            ans -= (
                1 << 32
            )  # Negative number adjustment as Python handles integers differently

        return ans
