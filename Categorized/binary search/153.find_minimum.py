from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        ans = float('inf')
        while l <= h:
            mid = (l + h) // 2

            if nums[l] <= nums[h]:
                ans = min(ans, nums[l])
                break
            

            if nums[l] <= nums[mid]:

                ans = min(ans, nums[l])
                l = mid + 1

            else:
                ans = min(ans, nums[mid])
                h = mid - 1
        return ans
    
s = Solution()
print(s.findMin([3,4,5,1,2]))