class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = matrix[i][j] + matrix[i - 1][j]
                else:
                    matrix[i][j] = 0

        s = Solution2()
        maximum = 0
        for row in matrix:
            maximum = max(maximum, s.largestRectangleArea(row))
        return maximum


# This is an extension of 84. Largest Rectangle in Histogram
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def previous_smaller_element(nums, pse, stack):

            for i in range(len(nums)):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                pse[i] = -1 if not stack else stack[-1]
                stack.append(i)
            return pse

        def next_smaller_element(nums, nse, stack):

            n = len(nums)
            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                nse[i] = n if not stack else stack[-1]
                stack.append(i)
            return nse

        n = len(heights)
        pse = [-1] * n
        nse = [-1] * n

        pse = previous_smaller_element(heights, pse, [])
        nse = next_smaller_element(heights, nse, [])
        # print(pse, nse)
        maximum = 0
        for i in range(n):
            maximum = max(maximum, (heights[i] * (nse[i] - pse[i] - 1)))

        return maximum
