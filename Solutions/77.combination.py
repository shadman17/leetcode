# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []

#         def backtrack(ind, arr):
#             if len(arr) == k:
#                 res.append(arr[:])
#                 return

#             if ind > n:
#                 return

#             arr.append(ind)
#             backtrack(ind+1, arr)
#             arr.pop()
#             backtrack(ind+1, arr)
        
#         backtrack(1, [])
#         return res
    
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(ind, arr):
            if len(arr) == k:
                res.append(arr[:])
                return

            for i in range(ind, n+1):
                arr.append(i)
                backtrack(i+1, arr)
                arr.pop()
        
        backtrack(1, [])
        return res
    
s = Solution()
print(s.combine(4,2))