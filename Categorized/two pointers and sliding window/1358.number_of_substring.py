class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        lastseen = [-1, -1, -1]
        count = 0
        for i in range(n):
            lastseen[ord(s[i]) - ord("a")] = i

            if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
                count += 1 + min(lastseen[0], lastseen[1], lastseen[2])

        return count


from typing import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        hashmap = defaultdict(int)
        l, r, count = 0, 0, 0

        while r < n:
            hashmap[s[r]] += 1

            while len(hashmap) == 3:
                count += n - r
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l += 1
            r += 1
        return count


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        arr = [0] * 3
        l, r, count = 0, 0, 0

        while r < n:
            arr[ord(s[r]) - ord("a")] += 1

            while arr[0] and arr[1] and arr[2]:
                count += n - r
                arr[ord(s[l]) - ord("a")] -= 1
                l += 1
            r += 1
        return count
