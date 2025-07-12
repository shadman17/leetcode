class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def backtrack(index, target, arr):
            if target == 0 and len(arr) == k:
                res.append(arr[:])
                return

            # if index > 9:
            #     return

            if index > 9 or index > target or len(arr) > k:
                return

            arr.append(index)
            backtrack(index + 1, target - index, arr)
            arr.pop()
            backtrack(index + 1, target, arr)

        backtrack(1, n, [])
        return res


# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         res = []

#         def dfs(i, summ, arr):
#             if summ == 0 and len(arr) == k:
#                 res.append(arr[:])

#             if summ < 0 or len(arr) >= k or i > 9:
#                 return

#             arr.append(i)
#             dfs(i+1, summ - i, arr)
#             arr.pop()
#             dfs(i+1, summ, arr)

#         dfs(1, n, list())

#         return res
