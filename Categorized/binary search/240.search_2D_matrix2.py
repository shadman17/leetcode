# Binary Search with O(n) * log(m)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        def binarysearch(arr):
            l, h = 0, c - 1

            while l <= h:
                mid = (l+h) // 2
                
                if arr[mid] == target:
                    return True

                elif arr[mid] < target:
                    l = mid + 1
                
                else:
                    h = mid - 1
            return False  

        for i in range(r):
            if matrix[i][0] <= target and target <= matrix[i][c-1]:
                x = binarysearch(matrix[i])
                if x:
                    return True

        return False
            
# Binary Search O(n+m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        row = 0
        col = c - 1
        while (row < r and col >= 0):
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False
