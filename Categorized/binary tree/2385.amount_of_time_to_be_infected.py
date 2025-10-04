# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}

        def bfs(root):
            q = deque([root])
            parent[root] = None
            while q:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    parent[node.left] = node
                if node.right:
                    q.append(node.right)
                    parent[node.right] = node

        def find_node(root, start: int):
            q = deque([root])
            while q:
                node = q.popleft()
                if node.val == start:
                    return node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        bfs(root)
        x = find_node(root, start)
        visited = set()
        q = deque()
        q.append((x, 0))
        answer = 0

        while q:
            node, time = q.popleft()
            if node.left and node.left not in visited:
                q.append((node.left, time + 1))
                visited.add(node.left)
            if node.right and node.right not in visited:
                q.append((node.right, time + 1))
                visited.add(node.right)
            if parent[node] and parent[node] not in visited:
                q.append((parent[node], time + 1))
                visited.add(parent[node])
            answer = max(answer, time)

        return answer
