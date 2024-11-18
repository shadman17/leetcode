class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_num = float("inf")
        start = 0
        end = 0
        length = len(nums)
        if length <= 1:
            return 0

        nums.sort()

        # print(nums)
        while end < length:

            if end - start + 1 < k:
                end += 1

            else:
                total = nums[end] - nums[start]
                min_num = min(min_num, total)
                start += 1
                end += 1

        return min_num
