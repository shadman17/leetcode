from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            if tuple(count) in ans:
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]

        return ans.values()


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = {}

#         for s in strs:

#             new_string = "".join(sorted(s))

#             if new_string in ans:
#                 ans[new_string].append(s)
#             else:
#                 ans[new_string] = [s]

#         return list(ans.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
