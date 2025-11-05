# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False

        def height(root):
            if not root:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)
            return max(leftheight, rightheight) + 1

        maxheight = height(root)

        q = deque()
        q.append(root)
        level = 1
        ans = 0
        while q and level <= maxheight:
            for _ in range(len(q)):
                node = q.popleft()
                if maxheight == level:
                    ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
            
        return ans
