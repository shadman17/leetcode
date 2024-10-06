from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq = [0] * 1001

        for num in nums1:
            freq[num] += 1

        ans = []
        for num in nums2:
            if freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans

# s = Solution()
# print(s.intersect([4,9,5], [9,4,9,8,4]))

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        intersection = []

        for num in nums2:
            if count1[num] > 0:
                intersection.append(num)
                count1[num] -= 1

        return intersection


s1 = Solution1()
print(s1.intersect([1, 2, 2, 1], [2,2]))