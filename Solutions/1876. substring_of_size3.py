from typing import List


class Solution:

    # def countGoodSubstrings(self, s: str) -> int:
    #     count=0
    #     for i in range(len(s)-2):
    #         if len(set(s[i:(i+3)]))==3:
    #             count+=1
    #     return count
    def countGoodSubstrings(self, s: str) -> int:
        start, end, window_size = 0, 0, 3

        count = 0
        arr = []

        while end < len(s):
            if end - start + 1 <= window_size:
                arr.append(s[end])
                end += 1

            else:
                if len(set(arr)) == 3:
                    count += 1

                arr.pop(0)
                start += 1

        if len(set(arr)) == 3:
            count += 1

        return count


s = Solution()
# print(s.countGoodSubstrings(s="xyzzaz"))
print(s.countGoodSubstrings(s="aababcabc"))
