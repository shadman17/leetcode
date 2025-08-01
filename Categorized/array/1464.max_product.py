class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums = [-val for val in nums]
#         print(nums)
#         heapq.heapify(nums)
#         print(nums)
#         return (heapq.heappop(nums) + 1) * (heapq.heappop(nums) + 1)
