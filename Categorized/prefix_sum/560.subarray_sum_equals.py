class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        presum = 0
        count = 0
        hashmap = {0: 1}

        n = len(nums)
        for i in range(n):
            presum += nums[i]
            diff = presum - k

            if diff in hashmap:
                count += hashmap[diff]

            hashmap[presum] = hashmap.get(presum, 0) + 1

        return count
