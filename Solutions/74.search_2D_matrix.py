from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         new_list = []

#         for x in matrix:
#             new_list.extend(x)

#         l, h = 0, len(new_list) - 1

#         while l <= h:
#             mid = (l + h) // 2

#             if new_list[mid] == target:
#                 return True

#             elif new_list[mid] < target:
#                 l = mid + 1

#             else:

#                 h = mid - 1

#         return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, h = 0, rows * cols - 1

        while l <= h:
            mid = l + (h - l) // 2
            r, c = mid // cols, mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = mid - 1
            else:
                l = mid + 1

        return False


s = Solution()
print(
    s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
)
print(
    s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
)
