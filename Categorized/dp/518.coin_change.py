from typing import List


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[-1] * (amount + 1) for _ in range(n)]

#         def memoization(i, target, dp):
#             if i == 0:
#                 if target % coins[0] == 0:
#                     return 1
#                 return 0

#             if dp[i][target] != -1:
#                 return dp[i][target]
#             not_pick = memoization(i - 1, target, dp)
#             pick = 0
#             if coins[i] <= target:
#                 pick = memoization(i, target - coins[i], dp)

#             dp[i][target] = not_pick + pick
#             return dp[i][target]

#         return memoization(n - 1, amount, dp)

# Tabulation

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0] * (amount + 1) for _ in range(n)]

#         for i in range(0, amount + 1):
#             if i % coins[0] == 0:
#                 dp[0][i] = 1

#         for i in range(1, n):
#             for amount_val in range(amount + 1):
#                 not_pick = dp[i - 1][amount_val]
#                 pick = 0
#                 if coins[i] <= amount_val:
#                     pick = dp[i][amount_val - coins[i]]
#                 dp[i][amount_val] = not_pick + pick
#         print(dp)
#         return dp[n - 1][amount]


# Space Optimized
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0] * (amount + 1)
        cur = [0] * (amount + 1)

        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1

        for i in range(1, n):
            for amount_val in range(amount + 1):
                not_pick = prev[amount_val]
                pick = 0
                if coins[i] <= amount_val:
                    pick = cur[amount_val - coins[i]]
                cur[amount_val] = not_pick + pick
            prev = cur[:]
        return prev[amount]


# Further Space Optimized
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0] * (amount + 1)

        for i in range(0, amount + 1):
            if i % coins[0] == 0:
                prev[i] = 1

        for i in range(1, n):
            for amount_val in range(amount + 1):
                not_pick = prev[amount_val]
                pick = 0
                if coins[i] <= amount_val:
                    pick = prev[amount_val - coins[i]]
                prev[amount_val] = not_pick + pick

        return prev[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         prev = [0] * (amount + 1)
#         prev[0] = 1

#         for coin in coins:
#             for j in range(coin, amount + 1):
#                 prev[j] += prev[j - coin]

#         return prev[amount]


s = Solution()
print(s.change(4, [1, 2, 3]))  # Expected output: 4
