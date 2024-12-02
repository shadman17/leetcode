from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        for char in nums1:
            if char in nums2:

                i = nums2.index(char)
                
                j = i+1
                added = False
                while j < len(nums2):
                    if nums2[j] > nums2[i]:
                        ans.append(nums2[j])
                        added = True
                        break
                    j+=1
                
                if not added:
                    ans.append(-1)

        return ans

s = Solution()

print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([2, 4], [1,2,3,4]))
# print(s.nextGreaterElement([4,1,2], [1,3,4,2]))