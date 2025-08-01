class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        j = 0
        for i in range(length * 2):
            ans.append(nums[j])
            j = j + 1
            if j == length:
                j = 0

        return ans
