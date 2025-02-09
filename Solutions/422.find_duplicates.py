from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        dict1 = {}

        for val in nums:
            dict1[val] = dict1.get(val, 0) + 1

        for key, value in dict1.items():
            if value == 2:
                result.append(key)

        return result
    
s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))
print(s.findDuplicates([1,1,2]))
print(s.findDuplicates([1]))
print(s.findDuplicates([]))
