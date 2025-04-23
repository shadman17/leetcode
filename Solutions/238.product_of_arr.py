from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for i in range(n)] 
        postfix = [1 for i in range(n)]
        result = [1 for i in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        return result

s = Solution()
print(s.productExceptSelf([1,2,3,4]))