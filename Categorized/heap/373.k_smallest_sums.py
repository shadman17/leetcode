import heapq
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        output = []
        minHeap = []
        for i in range(len(nums1)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))



        while k > 0:
            s, i, pos = heapq.heappop(minHeap)
            output.append([nums1[i], nums2[pos]])

            if pos + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[pos+1], i, pos+1))

            k -= 1
        
        return output
    
s = Solution()
print(s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))