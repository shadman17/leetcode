from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visit = [0] * len(nums)

        def dfs(arr):
            if len(nums) == len(arr):
                res.append(arr[:])

            for i in range(len(nums)):
                if visit[i]:
                    continue

                if i + 1 < len(nums) and nums[i] == nums[i+1] and visit[i+1]==0:
                    continue

                arr.append(nums[i])
                visit[i]=1
                dfs(arr)
                arr.pop()
                visit[i]=0


        dfs([])
        return res
        

s = Solution()
print(s.permuteUnique([1,1,2]))