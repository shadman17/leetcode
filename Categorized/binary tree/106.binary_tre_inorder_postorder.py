# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}  # value -> index in inorder

        def helper(inL: int, inR: int, postL: int, postR: int) -> Optional[TreeNode]:
            # empty range => no node
            if inL > inR or postL > postR:
                return None

            # root is the last element of current postorder slice
            root_val = postorder[postR]
            root = TreeNode(root_val)

            mid = idx[root_val]
            left_size = mid - inL

            root.left = helper(inL, mid - 1, postL, postL + left_size - 1)
            root.right = helper(mid + 1, inR, postL + left_size, postR - 1)

            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1 :], postorder[mid:-1])

        return root
