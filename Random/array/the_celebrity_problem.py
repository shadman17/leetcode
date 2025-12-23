class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        top = 0
        bottom = n - 1

        while top < bottom:
            if mat[top][bottom] == 1:
                top += 1

            elif mat[bottom][top] == 1:
                bottom -= 1

            else:
                top += 1
                bottom -= 1

        # if top > bottom:
        #     return -1
        for i in range(n):
            if mat[i][top] != 1:
                return -1
            if i != top and mat[top][i] != 0:
                return -1

        return top
