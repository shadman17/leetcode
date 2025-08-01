class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        
        return dfs(0)


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp = [0] * (n + 1)
#         print(dp)

#         dp[1], dp[2] = 1, 2

#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]

#         return dp[n]


s = Solution()
print(s.climbStairs(5))
