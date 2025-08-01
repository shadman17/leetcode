from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2
                
            if letters[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        if left < len(letters):
            return letters[left]
        else:
            return letters[0]
                
s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "c"))
print(s.nextGreatestLetter(["x","y","x", "y"], "c"))
print(s.nextGreatestLetter(["p", "p", "y", "y"], "x"))