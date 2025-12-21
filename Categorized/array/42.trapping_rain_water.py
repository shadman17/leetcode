class Solution:
    def trap(self, height: List[int]) -> int:
        def getleftmax(arr, height):
            arr[0] = height[0]
            for i in range(1, len(height)):
                arr[i] = max(height[i], arr[i - 1])

        def getrightmax(arr, height):
            n = len(height)
            arr[n - 1] = height[n - 1]
            for i in range(n - 2, -1, -1):
                arr[i] = max(height[i], arr[i + 1])

        n = len(height)
        leftmax = [-1] * n
        rightmax = [-1] * n
        getleftmax(leftmax, height)
        getrightmax(rightmax, height)

        total = 0
        for i in range(n):
            total += min(leftmax[i], rightmax[i]) - height[i]

        return total
