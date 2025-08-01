from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_strs = sorted(strs)

        x = new_strs[0]
        y = new_strs[len(strs) - 1]

        min_len = min(len(x), len(y))

        chars = ""
        for i in range(min_len):
            if x[i] != y[i]:
                return chars
            chars += x[i]

        return chars


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "floght"]))
