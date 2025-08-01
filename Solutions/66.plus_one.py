class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        length = len(digits)

        for i in range(length - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne("11", "1"))
