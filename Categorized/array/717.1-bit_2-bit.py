class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = 0
        n = len(bits)

        while l < n - 1:
            if bits[l] == 1:
                l += 2
            else:
                l += 1

        if l == n - 1:
            return True

        return False
