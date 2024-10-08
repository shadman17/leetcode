class Solution:
    def minSwaps(self, s: str) -> int:
        imbalanced = 0
        stack = []

        for char in s:
            if char == "[":
                stack.append(char)

            else:
                if stack:
                    stack.pop()
                else:
                    imbalanced += 1

        return (imbalanced + 1) // 2


s = Solution()
print(s.minSwaps("]]][[["))
