from typing import List
# Brute force

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i in range(len(arr)):
            if arr[i] <=k:
                k += 1                
            else:
                break
        
        return k
    
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         max_value = arr[-1]
#         hashset = set(arr)
#         count = 0
#         for i in range(max_value):
#             if i + 1 not in hashset:
#                 count += 1
#             if count == k:
#                 return i + 1
        
#         if count < k:
#             return (arr[-1] + k - count)
        

# binary Search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l = 0
        h = len(arr) - 1

        while l <= h:
            mid = (l + h) // 2

            missing = arr[mid] - mid - 1

            if missing < k:
                l = mid + 1
            else:
                h = mid - 1

        # return k + h + 1
        # or
        return l + k
        

s = Solution()
print(s.findKthPositive(arr = [3,4], k = 2))