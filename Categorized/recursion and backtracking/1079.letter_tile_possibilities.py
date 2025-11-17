class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hashmap = {}
        for c in tiles:
            hashmap[c] = hashmap.get(c, 0) + 1

        def backtrack(hashmap):
            res = 0
            for c in hashmap:
                if hashmap[c] > 0:
                    hashmap[c] -= 1
                    res += 1
                    res += backtrack(hashmap)
                    hashmap[c] += 1
            return res

        return backtrack(hashmap)