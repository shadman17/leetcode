# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            rightchild = node.right
            lastright = findlastright(node.left)
            lastright.right = rightchild

            return node.left

        def findlastright(node):
            if not node.right:
                return node
            return findlastright(node.right)

        dummy = root
        if not root:
            return None

        if root.val == key:
            return helper(root)

        while root:
            if key < root.val:
                if root.left is not None and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right

        return dummy
