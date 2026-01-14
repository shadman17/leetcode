from os import *
from sys import *
from collections import *
from math import *


def subsetSumToK(n, k, arr):

    def func(i, target, dp):
        if target == 0:
            return True

        if i == 0:
            return arr[0] == target

        if dp[i][target] != -1:
            return dp[i][target]

        not_pick = func(i - 1, target, dp)
        pick = False
        if arr[i] <= target:
            pick = func(i - 1, target - arr[i], dp)

        dp[i][target] = pick or not_pick
        return dp[i][target]

    return func(n - 1, k, [[-1] * (k + 1) for _ in range(n)])
