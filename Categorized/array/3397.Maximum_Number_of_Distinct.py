class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        count = 0
        prevmax = float("-inf")
        for num in arr:
            lowerbound = num - k
            upperbound = num + k

            if prevmax < lowerbound:
                prevmax = lowerbound
                count += 1

            elif prevmax < upperbound:
                prevmax += 1
                count += 1

        return count