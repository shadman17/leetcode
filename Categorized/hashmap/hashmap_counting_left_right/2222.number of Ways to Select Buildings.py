from collections import Counter
class Solution:
    def numberOfWays(self, s: str) -> int:
        res = 0
        left = Counter()
        right = Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]

            if s[i] == "0":
                if "1" in left and "1" in right:
                    res += left["1"] * right["1"]

            else:
                if "0" in left and "0" in right:
                    res += left["0"] * right["0"]

            left[s[i]] = left.get(s[i], 0) + 1
        
        return res