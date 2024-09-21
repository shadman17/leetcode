from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_strs = sorted(strs)

        x = new_strs[0]
        y = new_strs[len(strs) - 1]

        min_len = min(len(x), len(y))

        char = ""
        for i in range(min_len):
            if x[i] != y[i]:
                return char
            char += x[i]

        return char


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "floght"]))
