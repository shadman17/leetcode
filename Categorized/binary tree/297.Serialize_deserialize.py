# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        out = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                out.append("x")
            else:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(out)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i]!= 'x':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1


            if i < len(values) and values[i]!= 'x':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))