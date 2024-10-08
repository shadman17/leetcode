from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumB - sumA) // 2

        bobSizes.sort()

        for a in aliceSizes:
            b = a + diff

            left = 0 
            right = len(bobSizes) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if bobSizes[mid] == b:
                    return [a, b]
                
                elif bobSizes[mid] > b:
                    right = mid - 1

                else:
                    left = mid + 1


s = Solution()

print(s.fairCandySwap([1,1], [2,2]))
print(s.fairCandySwap([1,2], [2,3]))
print(s.fairCandySwap([2], [1,3]))
