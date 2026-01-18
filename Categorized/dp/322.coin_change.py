from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def memoization(i, target, dp):
            if i == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                return float("inf")

            if dp[i][target] != -1:
                return dp[i][target]

            not_pick = memoization(i - 1, target, dp)
            pick = float("inf")
            if coins[i] <= target:
                pick = 1 + memoization(i, target - coins[i], dp)

            dp[i][target] = min(not_pick, pick)
            return dp[i][target]

        res = memoization(n - 1, amount, [[-1] * (amount + 1) for _ in range(n)])
        return -1 if res == float("inf") else res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        for i in range(0, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = float("inf")

        for i in range(1, n):
            for j in range(amount + 1):
                not_pick = dp[i - 1][j]
                pick = float("inf")
                if coins[i] <= j:
                    pick = 1 + dp[i][j - coins[i]]
                dp[i][j] = min(not_pick, pick)
        return dp[n - 1][amount] if dp[n - 1][amount] != float("inf") else -1


# Space Optimized Version
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        prev = [-1] * (amount + 1)
        cur = [-1] * (amount + 1)
        for i in range(0, amount + 1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = float("inf")

        for i in range(1, n):
            for j in range(amount + 1):
                not_pick = prev[j]
                pick = float("inf")
                if coins[i] <= j:
                    pick = 1 + cur[j - coins[i]]
                cur[j] = min(not_pick, pick)

            prev = cur[:]
        return prev[amount] if prev[amount] != float("inf") else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))  # Expected output: 3
print(s.coinChange([2], 3))  # Expected output: -1
print(s.coinChange([1], 0))  # Expected output: 0
