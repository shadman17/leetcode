class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i] == 1:
                start = i
                break
        
        count = 0
        for i in range(start + 1, n):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1            
        return True
    

# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         if k == 0:
#             return True
#         prev = None
#         for i, num in enumerate(nums):
#             if num == 1:
#                 if prev is not None and i - prev <= k:
#                     return False
#                 prev = i
#         return True
