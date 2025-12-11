from typing import List
from collections import Counter
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        rmax = [0] * (n+1)
        rmin = [n+1] * (n+1)
        cmax = [0] * (n+1)
        cmin = [n+1] * (n+1)
        
        for x, y in buildings:
            rmax[x] = max(rmax[x], y)
            rmin[x] = min(rmin[x], y)
            cmax[y] = max(cmax[y], x)
            cmin[y] = min(cmin[y], x)
        

        res = 0
        for x, y in buildings:
            if rmin[x] < y < rmax[x] and cmin[y] < x < cmax[y]:
                res += 1


        return res

s = Solution()
print(s.countCoveredBuildings(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))