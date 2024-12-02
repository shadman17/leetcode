from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []
        for char in nums1:
            if char in nums2:

                i = nums2.index(char)

                j = i + 1
                added = False
                while j < len(nums2):
                    if nums2[j] > nums2[i]:
                        ans.append(nums2[j])
                        added = True
                        break
                    j += 1

                if not added:
                    ans.append(-1)

        return ans

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # hashmap = {}
        # result = []

        # for i in range(len(nums2)):
        #     cur = nums2[i]
        #     while stack and cur > stack[-1]:
        #         hashmap[stack[-1]] = cur
        #         stack.pop()

        #     stack.append(cur)

        # for element in stack:
        #     hashmap[element] = -1

        # for i in range(len(nums1)):
        #     result.append(hashmap[nums1[i]])

        # return result

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1_id = {n:i for i, n in enumerate(nums1)}
        # result = [-1] * len(nums1)
        # stack = []

        # length = len(nums2)
        # for i in range(length):
        #     cur = nums2[i]
        #     while stack and cur > stack[-1]:
        #         val = stack.pop()
        #         idx = nums1_id[val]
        #         result[idx] = cur

        #     if cur in nums1_id:
        #         stack.append(cur)

        # return result

s = Solution()

print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
# print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
