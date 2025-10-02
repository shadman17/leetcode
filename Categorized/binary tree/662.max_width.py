# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))

        ans = 0

        while q:
            first = last = 0
            length = len(q)
            for i in range(length):
                node, val = q.popleft()
                if i == 0:
                    first = val
                elif i == length - 1:
                    last = val

                if node.left:
                    q.append((node.left, 2 * val + 1))
                if node.right:
                    q.append((node.right, 2 * val + 2))

            ans = max(ans, last - first + 1)

        return ans

# if the input tree is big, the value 2*i will overflow! 
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         q = deque()
#         q.append((root, 0))

#         ans = 0

#         while q:
#             first = last = 0
#             length = len(q)
#             min_value = q[0][1]
#             for i in range(length):
#                 node, val = q.popleft()
#                 cur_id = val - min_value
#                 if i == 0:
#                     first = cur_id
#                 elif i == length - 1:
#                     last = cur_id

#                 if node.left:
#                     q.append((node.left, 2 * cur_id + 1))
#                 if node.right:
#                     q.append((node.right, 2 * cur_id + 2))

#             ans = max(ans, last - first + 1)

#         return ans
