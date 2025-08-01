# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        if not root:
            return self.result
        if not cur:
            return

        self.result.append(cur.val)
        self.preorderTraversal(cur.left)
        self.preorderTraversal(cur.right)

        return self.result


# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result: List[int] = []
#         self.traverse(root, result)
#         return result


#     def traverse(self, root: Optional[TreeNode], result: List[int]):
#         if not root:
#             return

#         result.append(root.val)
#         self.traverse(root.left, result)
#         self.traverse(root.right, result)
