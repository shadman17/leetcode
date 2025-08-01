# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
                
            if not node:
                return False
            total += node.val
            if not node.left and not node.right and total == targetSum:
                return True

            if dfs(node.left, total):
                return True
            if dfs(node.right, total):
                return True

            return False


        return dfs(root, 0)