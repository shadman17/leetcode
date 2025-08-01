from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.sum_matrix = [[0 for i in range(COLS+1)] for j in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c+1]
                self.sum_matrix[r+1][c+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2+1][col2+1] - self.sum_matrix[row1][col2+1] - self.sum_matrix[row2+1][col1] + self.sum_matrix[row1][col1] 

s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(s.sumRegion(2, 1, 4, 3))
print(s.sumRegion(1,1,2,2))


# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#         ROWS = len(matrix)
#         COLS = len(matrix[0])

#         self.sum_matrix = [[0 for i in range(COLS)] for j in range(ROWS)]

#         for i in range(ROWS):
#             for j in range(COLS):
#                 self.sum_matrix[i][j] = self.sum_matrix[i][j-1] + self.matrix[i][j] if j > 0 else self.matrix[i][j]

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         res = 0
#         for row in range(row1, row2+1):
#             res += self.sum_matrix[row][col2] - self.sum_matrix[row][col1-1] if col1 > 0 else self.sum_matrix[row][col2]

#         return res



# s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# print(s.sumRegion(2, 1, 4, 3))
# print(s.sumRegion(1,1,2,2))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)