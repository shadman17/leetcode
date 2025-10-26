class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])

        for i in range(r):
            for j in range(c):
                cur = mat[i][j]
                up = mat[i-1][j] if i > 0 else -1
                down = mat[i+1][j] if i < r - 1 else -1
                left = mat[i][j-1] if j > 0 else -1
                right = mat[i][j+1] if j < c - 1 else -1

                if cur > up and cur > down and cur > left and cur > right:
                    return [i, j]

