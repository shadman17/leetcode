from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

    # def reverseString(self, s: List[str]) -> None:
    #     s[:] = s[::-1]


s = Solution()
print(s.reverseString(s=["h", "e", "l", "l", "o"]))
print(s.reverseString(s=["H", "a", "N", "n", "a", "h"]))
