# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def isleaf(node):
            if not node.left and not node.right:
                return True
        
        q = deque()
        q.append(root)
        answer = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if isleaf(node):
                    return answer
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            answer += 1