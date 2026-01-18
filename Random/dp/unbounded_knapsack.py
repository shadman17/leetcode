# Memoization approach for Unbounded Knapsack Problem
class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)

        def memoization(i, w, dp):
            if i == 0:
                return (w // wt[0]) * val[0]

            if dp[i][w] != -1:
                return dp[i][w]

            not_take = memoization(i - 1, w, dp)
            take = float("-inf")
            if wt[i] <= w:
                take = val[i] + memoization(i, w - wt[i], dp)

            dp[i][w] = max(take, not_take)
            return dp[i][w]

        return memoization(n - 1, capacity, [[-1] * (capacity + 1) for _ in range(n)])


# Tabulation approach for Unbounded Knapsack Problem
class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)

        dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

        for w in range(0, capacity + 1):
            dp[0][w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(capacity + 1):
                not_take = dp[i - 1][w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + dp[i][w - wt[i]]

                dp[i][w] = max(take, not_take)

        return dp[n - 1][capacity]


# Space Optimized approach for Unbounded Knapsack Problem
class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)
        prev = [0] * (capacity + 1)
        cur = [0] * (capacity + 1)

        for w in range(0, capacity + 1):
            prev[w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(capacity + 1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + cur[w - wt[i]]

                cur[w] = max(take, not_take)
            prev = cur[:]

        return prev[capacity]


# space optimized version uses two 1D arrays to store previous and current states, reducing space complexity while maintaining the logic of the unbounded knapsack problem.


class Solution:
    def knapSack(self, val, wt, capacity):
        n = len(val)
        prev = [0] * (capacity + 1)

        for w in range(0, capacity + 1):
            prev[w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(capacity + 1):
                not_take = prev[w]
                take = float("-inf")
                if wt[i] <= w:
                    take = val[i] + prev[w - wt[i]]

                prev[w] = max(take, not_take)

        return prev[capacity]
