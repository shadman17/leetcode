# 1st_solution_in_my_mind
class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        
        def backtrack(ind, zerocount, arr):
            if len(arr) == n:
                res.append("".join(arr))
                return
            if zerocount < 1:
                arr.append("0")
                backtrack(ind + 1, zerocount+1, arr)
                arr.pop()
            
            zerocount = 0
            
            arr.append("1")
            backtrack(ind + 1, zerocount, arr)
            arr.pop()

        backtrack(0, 0, [])
        return res


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        
        def backtrack(arr):
            if len(arr) == n:
                res.append("".join(arr))
                return
            
            arr.append("1")
            backtrack(arr)
            arr.pop()
            
            if not arr or arr[-1] != "0":
                arr.append("0")
                backtrack(arr)
                arr.pop()

        backtrack([])
        return res


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def backtrack(curr):
            # If we've built a string of length n, record it
            if len(curr) == n:
                res.append(curr)
                return

            # Option 1: put '1' (always allowed)
            backtrack(curr + '1')

            # Option 2: put '0' (only if previous isn't '0')
            if not curr or curr[-1] != '0':
                backtrack(curr + '0')

        backtrack("")
        return res

