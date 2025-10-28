class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            cnt = 0
            while(n):
                n = n // 10
                cnt += 1
            
            if cnt % 2 == 0:
                count += 1
        
        return count