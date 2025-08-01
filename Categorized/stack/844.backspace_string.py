class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result1 = []
        result2 = []
        for i in range(len(s)):
            if s[i] != '#':
                result1.append(s[i])
            elif s[i] == '#' and result1:
                result1.pop()

        for i in range(len(t)):
            if s[i] != '#':
                result2.append(s[i])
            elif s[i] == '#' and result2:
                result2.pop()

        return result1 == result2
    
s = Solution()
print(s.backspaceCompare("a##c", "#a#c"))
print(s.backspaceCompare("xywrrmp", "xywrrmu#p"))