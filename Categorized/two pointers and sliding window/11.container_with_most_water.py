# Brute Force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculateArea(startIndex, endIndex, arr):
            area = (endIndex - startIndex) * min(arr[startIndex], arr[endIndex])
            return area


        maxx = 0
        length = len(height)
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                localMax = calculateArea(i, j, height)
                maxx = max(maxx, localMax)

        return maxx


# Optimal
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            min_val = min(height[l], height[r])
            result = max(result, min_val * (r-l))

            if height[l] >= height[r]:
                r -= 1
            else:
                l+=1
        
        return result
