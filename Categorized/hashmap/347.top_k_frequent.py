# Brute Force O(n log n)
from typing import List
from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         arr = list(count.items())
#         arr.sort(key=lambda x : (x[1], x[0]), reverse=True)

#         res = []
#         for i in range(k):
#             res.append(arr[i][0])
#         return res

# O (n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]
        
        for key, value in count.items():
            arr[value].append(key)

        result = []
        for i in range(len(arr) - 1, 0, -1):
            for val in arr[i]:
                result.append(val)
                if len(result) == k:
                    return result
        
s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))