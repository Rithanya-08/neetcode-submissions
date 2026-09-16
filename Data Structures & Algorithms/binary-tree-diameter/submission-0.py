# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        lefth = self.dfs(root.left)
        righth = self.dfs(root.right)
        self.diameter = max(self.diameter,lefth+righth)
        return 1 + max(lefth,righth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter