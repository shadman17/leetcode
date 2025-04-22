class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        prefix_sum, postfix_sum = 0, 0
        length = len(nums)

        postfix = [0] * length
        
        for i in range(length):
            prefix_sum += nums[i]
            prefix.append(prefix_sum)
        
        for i in range(length - 1, -1, -1):
            postfix_sum += nums[i]
            postfix[i] = postfix_sum

        for i in range(length):
            if prefix[i] == postfix[i]:
                return i
        
        return -1
    