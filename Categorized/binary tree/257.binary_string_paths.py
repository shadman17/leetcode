class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []

        def dfs(node, newstring):
            if not node:
                return
            newstring += str(node.val)
            if not node.left and not node.right:
                result.append(newstring)
            if node.left:
                dfs(node.left, newstring + "->")
            if node.right:
                dfs(node.right, newstring + "->")

        dfs(root, "")
        return result
