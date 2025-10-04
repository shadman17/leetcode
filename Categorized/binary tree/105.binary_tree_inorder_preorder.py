# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#O(n) with hashmap
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {v: i for i, v in enumerate(inorder)}

        def helper(prs, pre, ins, ine):
            if prs > pre or ins > ine:
                return None

            root = TreeNode(preorder[prs])
            inroot = hashmap[root.val]
            numsleft = inroot - ins

            root.left = helper(prs + 1, prs + numsleft, ins, inroot - 1)
            root.right = helper(prs + numsleft + 1, pre, inroot + 1, ine)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

#O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not preorder:
            return

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

