# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root
        while temp is not None:
            if val < temp.val:
                temp = temp.left
            elif val > temp.val:
                temp = temp.right
            else:
                return temp

        return None
