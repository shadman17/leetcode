from typing import Optional


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            print(ord(char))
            if ord(char) >= 97 and ord(char) <= 123:
                stack.append(char)

            elif ord(char) >= 48 and ord(char) <= 57 and stack:
                stack.pop()

        return ''.join(stack)


s = Solution()
print(s.clearDigits("abc21"))