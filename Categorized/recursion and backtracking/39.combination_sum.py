from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, arr):
            if total == target:
                res.append(arr[:])
                return
            if i >= len(candidates) or total > target:
                return

            arr.append(candidates[i])
            dfs(i, total + candidates[i], arr)
            arr.pop()
            dfs(i + 1, total, arr)

        dfs(0, 0, list())

        return res


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []

#         def dfs(i, total, arr):
#             if total == 0:
#                 res.append(arr[:])
#                 return
#             if i >= len(candidates) or total < 0:
#                 return

#             arr.append(candidates[i])
#             dfs(i, total - candidates[i], arr)
#             arr.pop()
#             dfs(i + 1, total, arr)

#         dfs(0, target, list())

#         return res


# s = Solution()
# print(s.combinationSum([2, 3, 6, 7], 7))
