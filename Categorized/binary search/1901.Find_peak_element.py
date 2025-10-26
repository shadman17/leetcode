# Brute Force
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

# Binary Search
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])

        # def maxelement(arr, r, mid):
        #     index = 0
        #     for i in range(1, r):
        #         if arr[i][mid] > arr[index][mid]:
        #             index = i
        #     return index

        def maxelement(arr, r, mid):
            maxx = -1
            maxvalue = -1
            for i in range(r):
                if arr[i][mid] > maxvalue:
                    maxx = i
                    maxvalue = arr[i][mid]
            return maxx


        l, h = 0, c - 1

        while l <= h:
            mid = (l + h) // 2
            row = maxelement(mat, r, mid)

            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if mid + 1 < c else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                h = mid - 1
            else:
                l = mid + 1
