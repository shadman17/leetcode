class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count1 = count2 = 0
        for char in nums:
            if char > 0:
                count1 += 1
            if char < 0:
                count2 += 1

        return max(count1, count2)
