# Definition for a binary tree node.
import heapq
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0, 0))
        col_table = defaultdict(list)
        result = []

        while q:
            for i in range(len(q)):
                node, row, col = q.popleft()
                heapq.heappush(col_table[row], (col, node.val))

                if node.left:
                    q.append((node.left, row - 1, col + 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))

        for col in sorted(col_table.keys()):
            col_values = []
            heap = col_table[col]
            while heap:
                col_values.append(heapq.heappop(heap)[1])

            result.append(col_values)

        return result

# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         q = deque()
#         q.append((root, 0, 0))
#         col_table = defaultdict(list)
#         result = []
#         while q:
#             for i in range(len(q)):
#                 node, x, y = q.popleft()
#                 col_table[x].append((y, node.val))

#                 if node.left:
#                     q.append((node.left, x - 1, y + 1))
#                 if node.right:
#                     q.append((node.right, x + 1, y + 1))

#         for col in sorted(col_table.keys()):
#             pairs = sorted(col_table[col])
#             col_values = []
#             for _, val in pairs:
#                 col_values.append(val)

#             result.append(col_values)


#         return result

# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         q = deque()
#         q.append((root, 0, 0))
#         col_table = defaultdict(list)
#         result = []
#         temp = []
#         while q:
#             for i in range(len(q)):
#                 node, row, col = q.popleft()
#                 col_table[row].append((col, node.val))

#                 if node.left:
#                     q.append((node.left, row - 1, col + 1))
#                 if node.right:
#                     q.append((node.right, row + 1, col + 1))

#         for col in sorted(col_table.keys()):
#             col_values = []
#             heap = col_table[col]
#             heapq.heapify(heap)
#             while heap:
#                 col_values.append(heapq.heappop(heap)[1])

#             result.append(col_values)


#         return result

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


values = [1, 2, 3, 4, 5, 6, 7]

root = build_tree(values)


s = Solution()
print(s.verticalTraversal(root))
