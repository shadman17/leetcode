# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.answer = []
        self.pointer = -1
        self.inorder(root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.answer.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        if not self.hasNext():
            return None
        self.pointer += 1
        return self.answer[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.answer) - 1

# O(h) instead of O(n)
# class BSTIterator:
#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         self.pushall(root)

#     def pushall(self,node):
#         while node:
#             self.stack.append(node)
#             node = node.left

#     def next(self) -> int:
#         temp = self.stack[-1]
#         self.stack.pop()
#         self.pushall(temp.right)
#         return temp.val

#     def hasNext(self) -> bool:
#         return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
