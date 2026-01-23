# Must solve LIS (count and generatino)


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n
        hashindex = [0] * n
        nums.sort()
        maxi = 1
        lastindex = 0
        for i in range(n):
            hashindex[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    hashindex[i] = j

            if dp[i] > maxi:
                maxi = dp[i]
                lastindex = i

        arr = [0] * maxi
        arr[0] = nums[lastindex]
        i = 1

        while hashindex[lastindex] != lastindex:
            lastindex = hashindex[lastindex]
            arr[i] = nums[lastindex]
            i += 1

        return list(reversed(arr))
