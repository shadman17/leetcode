class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        length = len(nums)
        count = 1
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                count += 1
                if count <= 2:
                    nums[k] = nums[i]
                    k += 1
            else:
                count = 1
                nums[k] = nums[i]
                k += 1
        return k