from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_heights = sorted(heights)

        count = 0 
        for i in range(len(new_heights)):
            if new_heights[i] != heights[i]:
                count += 1

        return count



s = Solution()
print(s.heightChecker([1,1,4,2,1,3]))
print(s.heightChecker([5,1,2,3,4]))
print(s.heightChecker([1,2,3,4,5]))

