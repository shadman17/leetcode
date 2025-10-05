# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []

        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        hashmap = {v: i for i, v in enumerate(result)}

        for i in range(len(result)):
            val = k - result[i]
            if val in hashmap and i != hashmap[val]:
                return True

        return False


# Two Pointer without hashmap
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         result = []
#         def inorder(node):
#             if not node:
#                 return None

#             inorder(node.left)
#             result.append(node.val)
#             inorder(node.right)

#         inorder(root)

#         first, second = 0, len(result) - 1

#         while first < second:
#             if result[first] + result[second] == k:
#                 return True

#             elif result[first] + result[second] > k:
#                 second -= 1

#             else:
#                 first += 1

#         return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class BSTiterator:
#     def __init__(self, root, reverse):
#         self.stack = []
#         self.reverse = reverse
#         self.pushall(root)

#     def pushall(self, node):
#         while node:
#             self.stack.append(node)
#             if self.reverse == True:
#                 node = node.right
#             else:
#                 node = node.left

#     def next(self):
#         temp = self.stack[-1]
#         self.stack.pop()
#         if not self.reverse:
#             self.pushall(temp.right)
#         else:
#             self.pushall(temp.left)

#         return temp.val

# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         l = BSTiterator(root, False)
#         r = BSTiterator(root, True)

#         i, j = l.next(), r.next()

#         while i < j:
#             if i + j == k:
#                 return True
#             elif i + j < k:
#                 i = l.next()
#             else:
#                 j = r.next()

#         return False


# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         if not root: return False
#         bfs, s = [root], set()
#         for i in bfs:
#             if k - i.val in s: return True
#             s.add(i.val)
#             if i.left: bfs.append(i.left)
#             if i.right: bfs.append(i.right)
#         return False
