# Optimal O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        map_nums = [0] * len(nums)

        def dfs(i, arr):

            if len(nums) == len(arr):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if map_nums[i] == 0:
                    map_nums[i] = 1
                    arr.append(nums[i])
                    dfs(i + 1, arr)
                    arr.pop()
                    map_nums[i] = 0

        dfs(0, [])
        return res


# Not optimal, O(n^2 * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for _, value in enumerate(nums):
                if value not in arr:
                    arr.append(value)
                    backtrack(arr)
                    arr.pop()

        backtrack([])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
