class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O":
                return

            board[r][c] = 1

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i in (0, m - 1) or j in (0, n - 1)):
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == 1:
                    board[i][j] = "O"
