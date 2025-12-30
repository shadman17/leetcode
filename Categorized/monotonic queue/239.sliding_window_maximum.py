from typing import List
from collections import deque


# Brute Force Approach
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         res = []
#         for i in range(n - k + 1):
#             new_nums = nums[i : i + k]
#             res.append(max(new_nums))
#         return res


# Deque Approach
# Time Complexity: O(N)
# Space Complexity: O(K)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()
        for i in range(n):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
