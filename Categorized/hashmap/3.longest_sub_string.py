class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        min_len = 0

        left = 0
        length = len(s)
        max_len = 0
        char_set = set()

        for right in range(length):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 0
        hashmap = defaultdict(int)
        max_len = 0

        while r < len(s):
            if hashmap[s[r]] != -1:
                if hashmap[s[r]] >= l:
                    l = hashmap[s[r]] + 1

            max_len = max(max_len, r - l + 1)
            hashmap[s[r]] = r
            r += 1

        return max_len
