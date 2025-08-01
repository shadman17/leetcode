class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr[:])
                return

            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
            dfs(i+1, arr)

        dfs(0, [])
        return res