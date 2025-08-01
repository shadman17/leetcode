class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num // 2

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid == num:
                return True

            elif mid * mid > num:
                right = mid - 1

            else:
                left = mid + 1

        return False


s = Solution()
print(s.isPerfectSquare(256))
