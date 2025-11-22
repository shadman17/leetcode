# O(n*n!)


class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0

        def backtrack(ind, arr, visited):
            if len(arr) == n:
                self.count += 1
                return

            for i in range(1, n + 1):
                if i not in visited and (i % ind == 0 or ind % i == 0):
                    visited.add(i)
                    arr.append(i)
                    backtrack(ind + 1, arr, visited)
                    arr.pop()
                    visited.remove(i)

        backtrack(1, [], set())
        return self.count


# # O(n ^ 2*n!)
# class Solution:
#     def countArrangement(self, n: int) -> int:
#         self.count = 0

#         def backtrack(ind, arr):
#             if len(arr) == n:
#                 self.count += 1
#                 return

#             for i in range(1, n + 1):
#                 if i not in arr and (i % ind == 0 or ind % i == 0):
#                     arr.append(i)
#                     backtrack(ind + 1, arr)
#                     arr.pop()

#         backtrack(1, [])
#         return self.count
