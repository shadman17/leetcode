class Solution:
    def minLength(self, s: str) -> int:
        
        for _ in range(len(s)):
            if "AB" in s:
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "")
        return len(s)


s = Solution()
print(s.minLength("ABFCACDB"))
print(s.minLength("ACBBD"))
