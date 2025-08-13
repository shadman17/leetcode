class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        minlen = float("inf")
        res = [-1, -1]
        count, window = {}, {}

        for char in t:
            count[char] = count.get(char, 0) + 1

        have, need = 0, len(count)

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

            r += 1

        l, r = res
        return s[l : r + 1] if minlen != float("inf") else ""
