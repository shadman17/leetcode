class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        list_s = list(s)

        list_g = list(goal)

        for i in range(len(list_s)):
            x = list_s.pop(0)
            list_s.append(x)

            if list_s == list_g:
                return True

        return False

s = Solution()
print(s.rotateString(s = "abcde", goal = "cdeab"))
print(s.rotateString(s = "abcde", goal = "abced"))