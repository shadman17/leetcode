from typing import *


# Memoization
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    dp = [[-1] * 4 for _ in range(n)]

    def memoization(day, last):

        if day == 0:
            maxi = 0

            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])

            return maxi

        if dp[day][last] != -1:
            return dp[day][last]

        maxi = 0
        for i in range(3):
            if i != last:
                ans = points[day][i] + memoization(day - 1, i)

                maxi = max(ans, maxi)

        dp[day][last] = maxi
        return dp[day][last]

    return memoization(n - 1, 3)


# Tabulation
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    dp = [[-1] * 4 for _ in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    ans = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], ans)

    return dp[n - 1][3]


# Space Optimization
from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:

    prev = [-1] * 4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        temp = [-1] * 4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task != last:
                    ans = points[day][task] + prev[task]
                    temp[last] = max(temp[last], ans)
        prev = temp
    return prev[3]
