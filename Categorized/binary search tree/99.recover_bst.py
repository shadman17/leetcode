# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.mid = self.second = self.prev = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.mid = node

                else:
                    self.second = node

            self.prev = node
            inorder(node.right)

        inorder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

        else:
            self.first.val, self.mid.val = self.mid.val, self.first.val
