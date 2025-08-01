class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_set = 'abcdefghijklmnopqrstuvwxyz1234567890'

        newstring = ''
        for char in s.lower():
            if char in string_set:
                newstring += char

        print(newstring)

        return newstring == newstring[::-1]
    
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("None"))
print(s.isPalindrome(""))