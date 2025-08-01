from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total_sum = 0

        for i in range(k):
            total_sum += nums[i]
        
        max_value = total_sum / k

        for i in range(len(nums) - k):
            total_sum = total_sum - nums[i] + nums[i+k]
            check_value = total_sum / k
            # print(check_value)
            max_value = max(max_value, check_value)

        return max_value

s = Solution()
# print(s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
# print(s.findMaxAverage(nums = [5], k = 1))
# print(s.findMaxAverage(nums = [0,4,0,3,2], k = 1))
print(s.findMaxAverage(nums = [4,2,1,3,3], k = 2))