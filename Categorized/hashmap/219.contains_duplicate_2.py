from collections import Counter
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # probably TLE
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True

        # return False

        index_hash = {}

        for i, value in enumerate(nums):
            if value in index_hash and abs(i - index_hash[value]) <= k:
                return True

            index_hash[value] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
