class Solution:
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
        print(pse, nse)
        maximum = 0
        for i in range(n):
            maximum = max(maximum, (heights[i] * (nse[i] - pse[i] - 1)))

        return maximum
