# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result: List[int] = []
#         self.traverse(root, result)
#         return result


#     def traverse(self, root: Optional[TreeNode], result: List[int]):
#         if not root:
#             return

#         self.traverse(root.left, result)
#         self.traverse(root.right, result)
#         result.append(root.val)
