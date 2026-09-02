# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(root == None):
            return None
        
        if(root == p or root == q):
            return root

        leftn = self.lowestCommonAncestor(root.left,p,q)
        rightn = self.lowestCommonAncestor(root.right,p,q)

        if(leftn != None and rightn != None):
            return root

        if(leftn != None):
            return leftn

        if(rightn != None):
            return rightn


        