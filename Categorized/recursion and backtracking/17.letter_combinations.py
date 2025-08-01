from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        digitmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        count = 0

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                nonlocal count
                count = count + 1
                res.append(curstr)
                return

            for c in digitmap[digits[i]]:
                backtrack(i + 1, curstr + c)

        if digits:
            backtrack(0, "")

        # print(count)
        return res


s = Solution()
print(s.letterCombinations("23"))
