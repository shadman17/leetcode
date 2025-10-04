# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k - 1]


# O(n) space omitted
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.answer
