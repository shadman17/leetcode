class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        arr = []

        def backtrack(l, r):
            if l + r == 2 *n:
                res.append("".join(arr))
                return

            if l < n:
                arr.append("(")
                backtrack(l+1, r)
                arr.pop()

            if r < l:
                arr.append(")")
                backtrack(l, r+1)
                arr.pop()                 

        backtrack(0, 0)
        return res