class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            count = Counter(nums[i: i+k])
            sort_arr = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
            total_sum = sum(key * value for key, value in sort_arr[:x])
            ans.append(total_sum)
        
        return ans