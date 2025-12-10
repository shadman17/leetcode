class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(complexity)
        root = complexity[0]

        for i in range(1, n):
            if complexity[i] <= root:
                return 0

        res = 1
        for i in range(1, n):
            res *= i
            res = (res % MOD)

        return res % MOD