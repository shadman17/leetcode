class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         res = []

#         def backtrack(node, target, arr):
#             if not node:
#                 return

#             arr.append(node.val)
#             target -= node.val
#             if not node.left and not node.right:
#                 if target == 0:
#                     res.append(arr[:])
#             else:
#                 if node.left:
#                     backtrack(node.left, target, arr)
#                 if node.right:
#                     backtrack(node.right, target, arr)

#             arr.pop()

#         backtrack(root, targetSum, [])
#         return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def backtrack(node, target, arr):
            if not node:
                return

            arr.append(node.val)

            if not node.left and not node.right:
                if target - node.val == 0:
                    res.append(arr[:])
                arr.pop()
                return
            if node.left:
                backtrack(node.left, target - node.val, arr)
            if node.right:
                backtrack(node.right, target - node.val, arr)

            arr.pop()

        backtrack(root, targetSum, [])
        return res
