from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, total, arr):
            if total == target:
                res.append(arr[:])
                return

            if i >= len(candidates) or total > target:
                return

            arr.append(candidates[i])
            dfs(i + 1, total + candidates[i], arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total, arr)

        dfs(0, 0, [])
        return res


s = Solution()
print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()

#         def dfs(i, total, arr):
#             if total == 0:
#                 res.append(arr[:])
#                 return

#             if i >= len(candidates) or total < 0:
#                 return

#             arr.append(candidates[i])
#             dfs(i + 1, total - candidates[i], arr)
#             arr.pop()

#             while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
#                 i += 1
#             dfs(i + 1, total, arr)

#         dfs(0, target, [])
#         return res


# s = Solution()
# print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
# print(s.combinationSum2(candidates=[1, 1, 1, 1, 1, 1], target=5))
