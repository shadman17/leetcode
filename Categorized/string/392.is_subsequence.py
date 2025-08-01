class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s = list(s)
        for i in range(len(t)):
            if len(s) != 0 and t[i] == s[0]:
                s.pop(0)

        return len(s) == 0

    # Two Pointer
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     sp = tp = 0

    #     while sp < len(s) and tp < len(t):
    #         if s[sp] == t[tp]:
    #             sp += 1
    #         tp += 1

    #     return sp == len(s)


s = Solution()
print(s.isSubsequence(s="", t="ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))
