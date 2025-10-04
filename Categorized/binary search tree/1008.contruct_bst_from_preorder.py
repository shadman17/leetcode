# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        hashmap = {v: i for i, v in enumerate(inorder)}

        def helper(prestart, preend, instart, inend):
            if prestart > preend or instart > inend:
                return None

            root = TreeNode(preorder[prestart])
            mid = hashmap[preorder[prestart]]
            nums_left = mid - instart

            root.left = helper(prestart + 1, prestart + nums_left, instart, mid - 1)
            root.right = helper(prestart + nums_left + 1, preend, mid + 1, inend)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

#         def helper(preorder, i, bound):
#             if i >= len(preorder) or preorder[i] > bound:
#                 return None, i

#             root = TreeNode(preorder[i])
#             i+=1
#             root.left, i = helper(preorder, i, root.val)
#             root.right, i = helper(preorder, i, bound)

#             return root, i

#         root, _ = helper(preorder, 0, float("inf"))
#         return root
