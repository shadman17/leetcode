from typing import List
# Brute Force
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def get_split_possible(nums, total_sum):
            count = 1
            cur_sum = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] <= total_sum:
                    cur_sum += nums[i]
                
                else:
                    count += 1
                    cur_sum = nums[i]

            return count


        l = max(nums)
        h = sum(nums)

        for i in range(l, h+1):
            cnt = get_split_possible(nums,i)

            if cnt <= k:
                return i
            
from typing import List
# Binary Search
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def get_split_possible(nums, total_sum):
            count = 1
            cur_sum = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] <= total_sum:
                    cur_sum += nums[i]
                
                else:
                    count += 1
                    cur_sum = nums[i]

            return count


        l = max(nums)
        h = sum(nums)

        while l <= h:
            mid = (l+h) // 2
            cnt = get_split_possible(nums,mid)
            if cnt <= k:
                h = mid - 1
            else:
                l = mid + 1
        
        return l
    
# Binary Search
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def get_split_possible(nums, total_sum):
            count = 1
            cur_sum = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] <= total_sum:
                    cur_sum += nums[i]
                
                else:
                    count += 1
                    cur_sum = nums[i]

            return count


        l = max(nums)
        h = sum(nums)

        while l <= h:
            mid = (l+h) // 2
            cnt = get_split_possible(nums,mid)
            if cnt <= k:
                h = mid - 1
            else:
                l = mid + 1
        
        return l