from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       nums2 = [nums[i] * nums[i] for i in range(len(nums))] 
       nums2.sort()
       return nums2


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))