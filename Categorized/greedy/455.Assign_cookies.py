class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l, r = 0, 0
        count = 0
        while l < len(s) and r < len(g):
            if g[r] <= s[l]:
                r += 1
                count += 1
            l += 1
        
        return count