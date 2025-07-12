class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def recursion(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0

            if cache[r][c] != -1:
                return cache[r][c]

            if r == rows - 1 and c == cols - 1:
                return 1

            right = recursion(r + 1, c, rows, cols, cache)
            down = recursion(r, c + 1, rows, cols, cache)

            cache[r][c] = right + down
            return cache[r][c]

        return recursion(0, 0, m, n, [[-1] * n for i in range(m)])

