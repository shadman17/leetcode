class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ""
        length = len(s)

        for i in range(length):
            l, r = i, i
            while l >= 0 and r < length and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    res = s[l : r + 1]

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < length and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    res = s[l : r + 1]

                l -= 1
                r += 1

        return res


s = Solution()
print(s.longestPalindrome("babad"))  # Output: "bab" or "aba
