# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         INT_MAX = (1 << 31) - 1
#         INT_MIN = 1 << 31
#         if dividend == divisor:
#             return 1

#         signed = True
#         if dividend < 0 and divisor > 0:
#             signed = False

#         if dividend >= 0 and divisor < 0:
#             signed = False

#         n = abs(dividend)
#         d = abs(divisor)

#         ans = 0
#         while n >= d:
#             count = 0

#             while n >= (d << (count + 1)):  # (n >= d * 2 ^ count + 1)
#                 count += 1

#             ans += 1 << count
#             n = n - (d << count)

#         if ans >= INT_MAX and signed == True:
#             return INT_MAX

#         if ans >= INT_MIN and signed == False:
#             return -(INT_MIN)

#         return ans if signed else -ans


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)

        # sign of result (True => positive)
        positive = not (
            (dividend < 0) ^ (divisor < 0)
        )  # XOR to determine if signs are different

        n = abs(dividend)
        d = abs(divisor)

        ans = 0
        while n >= d:
            count = 0
            while n >= (d << (count + 1)):  # (n >= d * 2 ^ (count + 1))
                count += 1
            ans += 1 << count  # add 2^count to the answer
            n -= d << count  # subtract d * 2^count from n

        res = ans if positive else -ans

        if res > INT_MAX:  # Clamp to 32-bit signed integer range
            return INT_MAX
        if res < INT_MIN:  # Clamp to 32-bit signed integer range
            return INT_MIN
        return res
