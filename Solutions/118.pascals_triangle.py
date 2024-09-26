from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []

        for i in range(numRows):
            newlist = [1] * (i + 1)

            for j in range(1, i):
                newlist[j] = final[i-1][j-1] + final[i-1][j]
            
            final.append(newlist)

        return final



s = Solution()
print(s.generate(5))
