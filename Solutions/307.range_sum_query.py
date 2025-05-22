from typing import List

class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.total = root.left.total + root.right.total
        return root 

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.total = val
            return
        
        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)

        root.total = root.left.total + root.right.total

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRange_helper(self.root, left, right)
        
    def sumRange_helper(self, root, left, right):
        if left <= root.L and root.R <= right:
            return root.total

        if right < root.L or left > root.R:
            return 0

        return self.sumRange_helper(root.left, left, right) + self.sumRange_helper(root.right, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)