# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parent = {}

        def parent_find(root, q):
            q.append(root)
            parent[root] = None
            while q:
                node = q.popleft()
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    parent[node.right] = node

        parent_find(root, deque())

        q = deque([(target, 0)])
        visited = set()
        result = []
        visited.add(target)

        while q:
            node, dis = q.popleft()

            if dis == k:
                result.append(node.val)
                continue

            if dis < k:
                if node.left and node.left not in visited:
                    q.append((node.left, dis + 1))
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    q.append((node.right, dis + 1))
                    visited.add(node.right)

                if parent[node] and parent[node] not in visited:
                    q.append((parent[node], dis + 1))
                    visited.add(parent[node])

        return result
