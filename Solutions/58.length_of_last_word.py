class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_str = s.split()
        return len(list_of_str[-1])


s = Solution()
print(s.lengthOfLastWord("Hello World"))
