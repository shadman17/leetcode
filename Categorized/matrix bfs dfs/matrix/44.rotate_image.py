# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)

#         for i in range(n):
#             for j in range(i, n):
#                 # Transpose the matrix
#                 temp = matrix[i][j]
#                 matrix[i][j] = matrix[j][i]
#                 matrix[j][i] = temp
#         # Now reverse each row
#         for row in matrix:
#             row.reverse()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        # We will do a circular movement
        while l < r:
            for i in range(r - l):
                t, b = l, r
                # save the topleft one, as it will be overriden
                topleft = matrix[t][l + i]
                # matrix top left should be replaced by bottom left
                matrix[t][l + i] = matrix[b - i][l]
                # matrix bottom left should be replaced by bottom right
                matrix[b - i][l] = matrix[b][r - i]
                # matrix bottom right should be replaced by top right
                matrix[b][r - i] = matrix[t + i][r]
                # matrix top right should be replaced by top left, but top left is already overriden, so we use topleft
                matrix[t + i][r] = topleft

            l += 1
            r -= 1
                
