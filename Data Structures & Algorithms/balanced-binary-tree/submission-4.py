# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,node : Optional[TreeNode]) ->int:
        if(node.right == None and node.left == None):
            return 0
        if(node.right != None and node.left != None):
            return 1+ max(self.height(node.left),self.height(node.right))
        if(node.right!=None):
            return 1+self.height(node.right)
        if(node.left!=None):
            return 1+self.height(node.left) 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True

        if(root.left == None and root.right == None):
            return True

        if(root.left != None and root.right != None):
            l = self.height(root.left)
            r = self.height(root.right)
        elif(root.left == None):
            l = -1
            r = self.height(root.right)
        else:
            r = -1
            l = self.height(root.left)

        if(abs(l - r) > 1):
            return False

       
        if(root.left and not self.isBalanced(root.left)):
            return False
        if(root.right and not self.isBalanced(root.right)):
            return False

        return True    
