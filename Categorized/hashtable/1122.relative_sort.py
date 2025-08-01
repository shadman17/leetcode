from collections import defaultdict
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countmap = {}
        end = []
        final = []
        for char in arr1:
            if char in arr2:
                countmap[char] = countmap.get(char, 0) + 1
            else:
                end.append(char)

        end.sort()

        for char in arr2:
            for _ in range(countmap[char]):
                final.append(char)

        return final + end


s = Solution()
# print(
#     s.relativeSortArray(
#         arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
#     )
# )
# print(s.relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
print(s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
