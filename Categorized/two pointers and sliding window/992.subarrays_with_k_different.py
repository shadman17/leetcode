from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def helper(hashmap, arr, target):
            l, r, count = 0, 0, 0
            n = len(arr)
            while r < n:
                hashmap[arr[r]] = hashmap.get(arr[r], 0) + 1

                while len(hashmap) > target:
                    hashmap[arr[l]] = hashmap.get(arr[l], 0) - 1
                    if hashmap[arr[l]] == 0:
                        del hashmap[arr[l]]
                    l += 1
                count += r - l + 1
                r += 1

            return count

        return helper({}, nums, k) - helper({}, nums, k - 1)


s = Solution()
print(s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
