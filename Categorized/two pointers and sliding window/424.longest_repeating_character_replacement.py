class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, r, maxlen = 0, 0, 0
        n = len(s)
        while r < n:
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen
