# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            root = new_node
            return root

        temp = root
        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    return root
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return root

                temp = temp.right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            root = new_node
            return root

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root