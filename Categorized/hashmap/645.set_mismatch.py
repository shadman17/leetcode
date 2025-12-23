from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        length = len(nums)        
        hashmap = {i:0 for i in range(1, length + 1)}


        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        duplicate, missing = 0, 0

        for key, value in hashmap.items():
            if value == 2:
                duplicate = key
            
            if value == 0:
                missing = key

        return [duplicate, missing]



s = Solution()
print(s.findErrorNums([1,2,4,4]))
print(s.findErrorNums([1,1]))
print(s.findErrorNums([1,3,3,4]))
