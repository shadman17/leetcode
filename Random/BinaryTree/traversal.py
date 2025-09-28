class Treenode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def traversal(self, root: Treenode):
        stack = []
        stack.append((root, 1))
        inorder = []
        preorder = []
        postorder = []

        while stack:
            node, num = stack.pop()

            if num == 1:
                preorder.append(node.value)
                stack.append((node, num + 1))
                if node.left is not None:
                    stack.append((node.left, 1))

            elif num == 2:
                inorder.append(node.value)
                stack.append((node, num + 1))
                if node.right is not None:
                    stack.append((node.right, 1))

            else:
                postorder.append(node.value)
        return preorder, inorder, postorder


node3 = Treenode(3)
node5 = Treenode(5)
node2 = Treenode(2, node3)
node4 = Treenode(4, None, node5)
node1 = Treenode(1, node2, node4)

s = Solution()
print(s.traversal(node1))
