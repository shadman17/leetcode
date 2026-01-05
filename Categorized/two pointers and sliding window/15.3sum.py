"""
Plan
# No duplicate triplets (I may use hashset or sort the list)
# Can return the output in any order

1. Sort the list
2. For each value, apply two sum with two pointer
3. if num[i] == nums[i - 1], we canskip to avoid duplicate or we can keep a
hashset to avoid duplicate
4. return the array
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1

        # print(res) # {(-1, 0, 1), (-1, -1, 2)}
        # return list(res) # [[-1,0,1],[-1,-1,2]]
        return [list(arr) for arr in res]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
