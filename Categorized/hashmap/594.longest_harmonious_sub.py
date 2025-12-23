from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        max_length = 0
        for val in counter:
            if val + 1 in counter:
                max_length = max(max_length, counter[val] + counter[val+1])

        return max_length


s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
print(s.findLHS([1,2,3,4]))
print(s.findLHS([1,1,1,1]))

