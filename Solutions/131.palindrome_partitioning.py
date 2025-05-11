class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def palindrome(s):
            return s == s[::-1]

        res = []

        def backtrack(ind, s, path):
            if ind == len(s):
                res.append(path[:])
                return

            for i in range(ind, len(s)):
                if palindrome(s[ind : i + 1]):
                    path.append(s[ind : i + 1])
                    backtrack(i + 1, s, path)
                    path.pop()

        backtrack(0, s, [])
        return res
