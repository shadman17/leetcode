from typing import List

# class Solution:
#     def countPartitions(self, nums: List[int]) -> int:
#         count = 0
#         n = len(nums)
#         for i in range(0, n - 1):
#             summ1 = sum(nums[0 : i + 1])
#             summ2 = sum(nums[i + 1 : n])

#             print(summ1, summ2)

#             result = abs(summ1 - summ2)

#             count += 1 if result % 2 == 0 else 0

#         return count


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        summ = sum(nums)
        leftsum = 0
        rightsum = 0
        for i in range(n - 1):
            leftsum += nums[i]
            rightsum = summ - leftsum

            result = abs(rightsum - leftsum)

            count += 1 if result % 2 == 0 else 0

        return count


s = Solution()
print(s.countPartitions([10, 10, 3, 7, 6]))
