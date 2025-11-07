
# Recursion O(N ^ N)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         def getTotal(ind, jumps):
#             if ind >= len(nums) - 1:
#                 return jumps
            
#             mini = float("inf")
#             for i in range(1, nums[ind] + 1):
#                 mini = min(mini, getTotal(ind + i, jumps + 1))

#             return mini
#         return getTotal(0, 0)

# Greedy O(n)

# Recursion O(N ^ N)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         def getTotal(ind, jumps):
#             if ind >= len(nums) - 1:
#                 return jumps
            
#             mini = float("inf")
#             for i in range(1, nums[ind] + 1):
#                 mini = min(mini, getTotal(ind + i, jumps + 1))

#             return mini
#         return getTotal(0, 0)

# Greedy O(n)
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, jumps = 0, 0, 0
        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
                
            l = r + 1
            r = far
            jumps += 1
        return jumps

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([1,2,1,1,1]))
