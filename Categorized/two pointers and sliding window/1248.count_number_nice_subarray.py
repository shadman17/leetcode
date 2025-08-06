class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        def helper(nums, x):
            if x < 0:
                return 0
            l, r, count, total = 0, 0, 0, 0
            n = len(nums)
            while r < n:
                if nums[r] == 1:
                    total += 1

                while total > x:
                    total -= nums[l]
                    l += 1

                count += r - l + 1
                r += 1
            return count

        return helper(nums, k) - helper(nums, k - 1)


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def helper(nums, x):
            if x < 0:
                return 0
            l, r, count, total = 0, 0, 0, 0
            n = len(nums)
            while r < n:
                total += nums[r]

                while total > x:
                    total -= nums[l]
                    l += 1

                count += r - l + 1
                r += 1
            return count

        return helper(nums, k) - helper(nums, k - 1)
