# class Solution:
#     def isHappy(self, n: int) -> bool:

#         slow = n
#         fast = self.next_number(n)

#         while slow != fast:

#             slow = self.next_number(slow)
#             fast = self.next_number(self.next_number(fast))

#         return slow == 1

#     def next_number(self, n):
#         total_sum = 0
#         while n:
#             remainder = n % 10
#             total_sum += remainder * remainder
#             n = n // 10

#         return total_sum


# s = Solution()
# print(s.isHappy(2))


class Solution1:
    def isHappy(self, n: int) -> bool:

        new_dict = {}

        while True:
            if new_dict.get(n) == True:
                return False
            new_dict[n] = True
            print(new_dict)
            n = self.next_number(n)

            if n == 1:
                return True

        return False

    def next_number(self, n):
        total_sum = 0
        while n:
            remainder = n % 10
            total_sum += remainder * remainder
            n = n // 10

        return total_sum


s1 = Solution1()
print(s1.isHappy(2))
