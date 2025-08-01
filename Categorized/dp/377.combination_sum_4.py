
class Solutions:
    def test(self, nums, target):
        memo = {}
        def dfs(total):
            if total == target:
                return 1
            
            if total > target:
                return 0

            if total in memo:
                return memo[total]

            count = 0
            for i in range(len(nums)):
                count += dfs(total+nums[i])

            memo[total] = count
            return count

        return dfs(0) 


# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         memo = {}
#         def dfs(remainder):
#             if remainder == 0:
#                 return 1
            
#             if remainder < 0:
#                 return 0

#             if remainder in memo:
#                 return memo[remainder]

#             count = 0
#             for i in range(len(nums)):
#                 count += dfs(remainder-nums[i])

#             memo[remainder] = count
#             return count

#         return dfs(target) 

s = Solutions()
print(s.test([1,2,3], 4))           