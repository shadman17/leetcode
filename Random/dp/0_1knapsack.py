class Solution:
    def knapsack(self, W, val, wt):
        # code here

        n = len(val)

        # def memoization(i, w, dp):
        #     if i == 0:
        #         if wt[0] <= w:
        #             return val[0]

        #         else:
        #             return 0
        #     if dp[i][w] != -1:
        #         return dp[i][w]
        #     not_take = memoization(i - 1, w, dp)
        #     take = float("-inf")
        #     if wt[i] <= w:
        #         take = val[i] + memoization(i - 1, w - wt[i], dp)

        #     dp[i][w] = max(take, not_take)
        #     return dp[i][w]

        # return memoization(n - 1, W, [[-1] * (W + 1) for _ in range(n)])

        def tabulation():
            dp = [[0 for _ in range(W + 1)] for _ in range(n)]

            for w in range(wt[0], W + 1):
                dp[0][w] = val[0]

            for i in range(1, n):
                for w in range(W + 1):
                    not_take = dp[i - 1][w]
                    take = float("-inf")
                    if wt[i] <= w:
                        take = val[i] + dp[i - 1][w - wt[i]]

                    dp[i][w] = max(take, not_take)

            return dp[n - 1][W]

        return tabulation()


# Space Optimized
class Solution:
    def knapsack(self, W, val, wt):
        # code here

        n = len(val)
        prev = [0] * (W + 1)
        cur = [0] * (W + 1)

        for w in range(wt[0], W + 1):
            prev[w] = val[0]

        for i in range(1, n):
            for w in range(W + 1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + prev[w - wt[i]]

                cur[w] = max(take, not_take)

            prev = cur[:]

        return prev[W]


# space optimized 2
class Solution:
    def knapsack(self, W, val, wt):
        # code here

        n = len(val)
        prev = [0] * (W + 1)

        for w in range(wt[0], W + 1):
            prev[w] = val[0]

        for i in range(1, n):
            for w in range(W, -1, -1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + prev[w - wt[i]]

                prev[w] = max(take, not_take)

        return prev[W]
