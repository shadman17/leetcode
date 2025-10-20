class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divisor(nums, divisor):
            answer = 0
            for i in range(len(nums)):
                answer += math.ceil(nums[i] / divisor)
            
            return answer

        l = 1
        h = -1
        for i in range(len(nums)):
            if nums[i] > h:
                h = nums[i]
        ans = 0
        while l <= h:
            mid = (l + h) // 2

            value = divisor(nums, mid)

            if value > threshold:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1

        return ans

            

