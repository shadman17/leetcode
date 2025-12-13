class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l, r = 0, 0
        n = len(s)
        length = len(p)
        hashmap1 = Counter(p)
        hashmap2 = Counter()
        while r < n:
            if s[r] not in hashmap1:
                r += 1
                continue
            else:
                hashmap2[s[r]] = hashmap2.get(s[r], 0) + 1
                while r - l + 1 > length:
                    if s[l] in hashmap2:
                        hashmap2[s[l]] -= 1
                        if hashmap2[s[l]] == 0:
                            del hashmap2[s[l]]
                    l += 1
                if hashmap1 == hashmap2:
                    res.append(l)
                r += 1
        return res
