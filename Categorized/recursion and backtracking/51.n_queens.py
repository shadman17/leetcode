class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(r, board, col, posDiag, negDiag, res):

            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1, board, col, posDiag, negDiag, res)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

            return res

        board = [["."] * n for i in range(n)]

        return backtrack(0, board, set(), set(), set(), [])
