class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i, sub):
            if len(sub) == len(s):
                res.append(sub)
                return
            
            if s[i].isalpha():
                dfs(i+1, sub+s[i].swapcase())
            
            dfs(i+1, sub+s[i])

        dfs(0, "")
        return res