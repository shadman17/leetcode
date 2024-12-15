from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        result = [-1] * len(nums)
        stack = []
        length = len(nums)

        for i in range(2 * length):
            cur = nums[i%length]

            while stack and cur > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = cur
            
            if i < length:
                stack.append(i)

        return result
    
# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
#         stack, res = [], [-1] * len(nums)
#         for i, num in enumerate(nums):              # 2
#             while stack and nums[stack[-1]] < num:
#                 res[stack.pop()] = num
#             stack.append(i)
#         for i, num in enumerate(nums):              # 3
#             while stack and nums[stack[-1]] < num:
#                 res[stack.pop()] = num
#         return res

s = Solution()
print(s.nextGreaterElements(nums = [1,2,1]))
print(s.nextGreaterElements(nums = [1,2,3,4,3]))
# print(s.nextGreaterElements())