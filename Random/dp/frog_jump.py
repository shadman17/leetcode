class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        dp = [-1] * (n + 1)

        # Memoization

        # def jump(ind, height):
        #     if ind == 0:
        #         return 0

        #     if dp[ind] != -1:
        #         return dp[ind]

        #     right = 100001
        #     left = jump(ind - 1, height) + abs(height[ind] - height[ind - 1])
        #     if ind > 1:
        #         right = jump(ind - 2, height) + abs(height[ind] - height[ind - 2])

        #     dp[ind] = min(left, right)
        #     return dp[ind]

        # return jump(n - 1, height)

        # Tabulation
        # n = len(height)
        # dp = [-1] * (n)
        # def jump(height):
        #     dp[0] = 0
        #     for ind in range(1, n):
        #         left = dp[ind - 1] + abs(height[ind] - height[ind - 1])
        #         right = 100001
        #         if ind > 1:
        #             right = dp[ind - 2] + abs(height[ind] - height[ind - 2])
        #         dp[ind] = min(left, right)

        #     return dp[n - 1]

        # return jump(height)

        # Space optimization
        n = len(height)
        dp = [-1] * (n)

        def jump(height):
            prev, prev2 = 0, 0
            for ind in range(1, n):
                left = prev + abs(height[ind] - height[ind - 1])
                right = 100001
                if ind > 1:
                    right = prev2 + abs(height[ind] - height[ind - 2])

                cur = min(left, right)
                prev2 = prev
                prev = cur

            return prev

        return jump(height)
