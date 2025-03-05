class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


# class Solution:
#     def fib(self, n: int) -> int:
#         result = [0] * 31
#         result[1] = 1

#         for i in range(2, n + 1):
#             result[i] = result[i - 1] + result[i - 2]

#         return result[n]
