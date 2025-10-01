"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

from collections import defaultdict, deque


class Solution:
    def bottomView(self, root):

        q = deque([(root, 0)])
        hashmap = {}
        min_hd = max_hd = 0
        result = []
        while q:
            node, x = q.popleft()

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
