# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def max_depth(node):
            if not node:
                return 0
            return 1 + max(max_depth(node.left), max_depth(node.right))

        depth = max_depth(root)

        def dfs(node, curdepth):
            if not node:
                return None
            if not node.left and not node.right and curdepth == depth:
                return node

            left = dfs(node.left, curdepth + 1)
            right = dfs(node.right, curdepth + 1)

            if left and right:
                return node

            return left if left else right

        return dfs(root, 1)
