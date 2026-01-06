# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            queue = deque()
            queue.append(root)

            max_sum = -100001
            ans = 0
            level = 1

            while queue:
                cursum = 0
                for i in range(len(queue)):
                    curr = queue.popleft()
                    cursum += curr.val
                    print(f"{level} and {cursum}")
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                if cursum > max_sum:
                    ans = level
                    max_sum = cursum
                level += 1

            return ans

        return bfs(root)
