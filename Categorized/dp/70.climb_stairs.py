class Solution:
    def climbStairs(self, n: int) -> int:

        arr = [-1] * (n + 1)

        def dp(n, arr):
            if n == 0 or n == 1:
                return 1

            if arr[n] != -1:
                return arr[n]

            left = dp(n - 1, arr)
            right = dp(n - 2, arr)

            arr[n] = left + right

            return arr[n]

        return dp(n, arr)


# Memoization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         dp[0], dp[1] = 1, 1

#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]

#         return dp[n]


# Space Optimization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         prev, prev2 = 1, 1

#         for i in range(2, n + 1):
#             cur = prev + prev2
#             prev2 = prev
#             prev = cur

#         return prev


s = Solution()
print(s.climbStairs(5))
