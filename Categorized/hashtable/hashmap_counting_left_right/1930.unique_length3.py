class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        hashmap = Counter(s)
        for i in range(len(s)):
            hashmap[s[i]] -= 1

            for c in left:
                if hashmap[c] > 0:
                    res.add((c, s[i], c))

            left.add(s[i])

        return len(res)
