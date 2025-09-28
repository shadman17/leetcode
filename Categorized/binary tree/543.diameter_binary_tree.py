# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0

        def helper(root):
            if root == None:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            nonlocal maximum
            maximum = max(maximum, l + r)

            return 1 + max(l, r)

        helper(root)
        return maximum
