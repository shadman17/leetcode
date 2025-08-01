class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        max_perimeter = 0

        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                max_perimeter = max(max_perimeter, nums[i - 2] + nums[i - 1] + nums[i])

        return max_perimeter
