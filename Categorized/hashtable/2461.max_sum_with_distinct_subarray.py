class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        length = len(nums)
        hashmap = defaultdict(int)
        max_sum = 0
        window_sum = 0

        for end in range(length):
            window_sum += nums[end]
            hashmap[nums[end]] += 1
            # print(hashmap)

            if end - start + 1 == k:
                if len(hashmap) == k:
                    max_sum = max(window_sum, max_sum)

                window_sum -= nums[start]
                hashmap[nums[start]] -= 1
                if hashmap[nums[start]] == 0:
                    del hashmap[nums[start]]

                start += 1

        return max_sum
