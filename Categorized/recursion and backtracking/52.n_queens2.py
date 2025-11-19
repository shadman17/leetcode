# Extension of the previous n queens with count

# class Solution:
#     def totalNQueens(self, n: int) -> int:
# I can use visited set instead of board. I can do visited.add((r, c))
#         def backtrack(r, board, col, posDiag, negDiag):
#             total = 0

#             if r == n:
#                 return 1

#             for c in range(n):
#                 if c in col or (r + c) in posDiag or (r - c) in negDiag:
#                     continue

#                 board[r][c] = "Q"
#                 col.add(c)
#                 posDiag.add(r + c)
#                 negDiag.add(r - c)

#                 total += backtrack(r + 1, board, col, posDiag, negDiag)

#                 board[r][c] = "."
#                 col.remove(c)
#                 posDiag.remove(r + c)
#                 negDiag.remove(r - c)

#             return total

#         board = [["."] * n for r in range(n)]
#         return backtrack(0, board, set(), set(), set())


# I think I do not need the board array to store or any visited set!!!
class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(r, col, posDiag, negDiag):
            total = 0

            if r == n:
                return 1

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                total += backtrack(r + 1, col, posDiag, negDiag)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

            return total

        return backtrack(0, set(), set(), set())
