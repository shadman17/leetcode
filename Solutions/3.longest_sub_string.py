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
            max_len = max(max_len, right-left+1)

        return max_len