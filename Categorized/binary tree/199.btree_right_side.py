# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            right = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    right = cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            if right:
                res.append(right.val)

        return res
