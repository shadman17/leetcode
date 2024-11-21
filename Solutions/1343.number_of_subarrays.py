from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        length = len(arr)
        total_sum = sum(arr[:k])
        total_sub = total_sum / k

        count = 0

        for r in range(k, length):
            if total_sub >= threshold:
                count += 1

            total_sum = total_sum - arr[l] + arr[r]
            total_sub = total_sum / k

            l += 1

        if total_sub >= threshold:
            count += 1

        return count


s = Solution()
# print(s.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
# print(s.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
print(s.numOfSubarrays(arr=[7, 7, 7, 7, 7, 7, 7], k=7, threshold=7))
