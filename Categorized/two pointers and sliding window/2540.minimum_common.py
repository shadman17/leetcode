from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = r = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                return nums1[l]

            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return -1


# class Solution:
# def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#     nums1 = set(nums1)
#     nums2 = set(nums2)

#     nums3 = nums1.intersection(nums2)

#     nums3 = sorted(nums3)

#     return nums3[0] if nums3 else -1

# class Solution:
#     def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
#         i,j=0,0
#         while i<len(nums1) and j<len(nums2):
#             if nums1[i]==nums2[j]:
#                 return nums1[i]
#             else:
#                 if nums1[i]<nums2[j]:
#                     while i<len(nums1) and nums1[i]<nums2[j]:
#                         i+=1
#                 else:
#                     while j<len(nums2) and nums1[i]>nums2[j]:
#                         j+=1
#         return -1


s = Solution()
print(s.getCommon(nums1=[1, 2, 3], nums2=[2, 4]))
print(s.getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
print(
    s.getCommon(
        nums1=[
            1,
            2,
            3,
        ],
        nums2=[4, 5],
    )
)
