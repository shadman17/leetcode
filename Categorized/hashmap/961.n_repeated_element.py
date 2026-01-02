class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        find_count = n // 2

        hashmap = Counter(nums)

        for key in hashmap.keys():
            if hashmap[key] == find_count:
                return key
