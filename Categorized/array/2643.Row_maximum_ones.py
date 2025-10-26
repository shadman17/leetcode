# Brute Force
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max1 = -1
        row = -1

        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1

            if count > max1:
                max1 = count
                row = i

        return [row, max1]
    