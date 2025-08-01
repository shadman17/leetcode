class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def recursion(r, c, rows, cols, cache):
            if r == rows or c == cols or obstacleGrid[r][c]:
                return 0

            if cache[r][c] != -1:
                return cache[r][c]

            if r == rows - 1 and c == cols - 1:
                return 1

            right = recursion(r + 1, c, rows, cols, cache)
            down = recursion(r, c + 1, rows, cols, cache)

            cache[r][c] = right + down
            return cache[r][c]

        return recursion(
            0,
            0,
            len(obstacleGrid),
            len(obstacleGrid[0]),
            [[-1] * (len(obstacleGrid[0])) for i in range(len(obstacleGrid))],
        )
