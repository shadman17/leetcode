from collections import Counter
from typing import List
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        res = 0

        right = Counter(nums)
        left = Counter()
        for i in range(n):
            right[nums[i]] -= 1
            
            target = nums[i] * 2

            if target in left and target in right:
                res = (res + left[target] * right[target]) % MOD

            left[nums[i]] = left.get(nums[i], 0) + 1          
        return res % MOD
    
