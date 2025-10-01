# Definition for a binary tree node.
import heapq
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


from collections import defaultdict, deque


class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        q = deque()
        q.append((root, 0))
        hashmap = {}
        result = []
        min_hd = max_hd = 0
        while q:
            for i in range(len(q)):
                node, x = q.popleft()
                if x not in hashmap:
                    hashmap[x] = node.data
                    if x < min_hd:
                        min_hd = x
                    if x > max_hd:
                        max_hd = x
                if node.left:
                    q.append((node.left, x - 1))
                if node.right:
                    q.append((node.right, x + 1))

        for x in range(min_hd, max_hd + 1):
            result.append(hashmap[x])

        return result


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


values = [10, 20, 30, 40, 60, 90, 100]

root = build_tree(values)


s = Solution()
print(s.topView(root))
