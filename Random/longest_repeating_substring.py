# Longest Repeating substring with no duplicate
# Leetcode Premium Question
# Sliding Window

from collections import defaultdict


class Solution:
    def longestNonRepeatingSubstring(self, s):
        # your code goes here
        l, r, maxlen = 0, 0, 0
        hashmap = defaultdict(int)
        length = len(s)

        while r < length:
            hashmap[s[r]] += 1
            while hashmap[s[r]] > 1:
                hashmap[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen


s = Solution()
print(s.longestNonRepeatingSubstring("abcddabac"))
