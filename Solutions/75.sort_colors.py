class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, h = 0, 0, len(nums) - 1

        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         counts = [0,0,0]
#         for i in range(len(nums)):
#             counts[nums[i]] += 1

#         m = 0
#         for i in range(3):
#             for j in range(counts[i]):
#                 nums[m] = i
#                 m+=1

# class Solution(object):
#     def sortColors(self, nums):
#         r=nums.count(0)
#         w=nums.count(1)
#         g=nums.count(2)
#         k=0
#         for i in range(r):
#             nums[k]=0
#             k+=1

#         for i in range(w):
#             nums[k]=1
#             k+=1
#         for i in range(g):
#             nums[k]=2
#             k+=1
