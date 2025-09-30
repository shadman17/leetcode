"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:
    def boundaryTraversal(self, root):
        # Code here
        result = []
        result.append(root.data)

        def isleaf(root):
            if root.left is None and root.right is None:
                return True
            return False

        def leftboundary(root):
            cur = root.left
            while cur:
                if not isleaf(cur):
                    result.append(cur.data)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right

        def rightboundary(root):
            temp = []
            cur = root.right
            while cur:
                if not isleaf(cur):
                    temp.append(cur.data)
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left

            result.extend(temp[::-1])

        def leafnode(node):
            if isleaf(node):
                if node is not root:
                    result.append(node.data)
                    return
            if node.left:
                leafnode(node.left)
            if node.right:
                leafnode(node.right)

        leftboundary(root)
        leafnode(root)
        rightboundary(root)

        return result
