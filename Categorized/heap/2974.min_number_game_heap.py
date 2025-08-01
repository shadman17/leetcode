class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heapq.heapify(nums)

        for _ in range(len(nums) // 2):
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            arr.append(second)
            arr.append(first)

        return arr
