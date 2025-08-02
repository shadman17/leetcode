from collections import defaultdict
from typing import List

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         l, r, maxlen = 0, 0, 0
#         hashmap = defaultdict(int)

#         while r < len(fruits):
#             hashmap[fruits[r]] += 1

#             while len(hashmap) > 2:

#                 hashmap[fruits[l]] -= 1
#                 if hashmap[fruits[l]] == 0:
#                     del hashmap[fruits[l]]
#                 l += 1

#             maxlen = max(maxlen, r - l + 1)
#             r += 1
#         return maxlen


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r, maxlen = 0, 0, 0
        hashmap = defaultdict(int)

        while r < len(fruits):
            hashmap[fruits[r]] += 1

            if len(hashmap) > 2:

                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen


s = Solution()
print(s.totalFruit(fruits=[1, 2, 1]))
print(s.totalFruit(fruits=[0, 1, 2, 2]))
print(s.totalFruit([1, 2, 3, 3, 2, 2, 1, 2, 2]))
