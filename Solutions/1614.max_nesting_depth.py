class Solution:
    def maxDepth(self, s: str) -> int:
        count, max_num = 0, 0
        for char in s:
            if char == '(':
                count += 1

                max_num = max(max_num, count)

            elif char == ')':
                count -= 1

        return max_num