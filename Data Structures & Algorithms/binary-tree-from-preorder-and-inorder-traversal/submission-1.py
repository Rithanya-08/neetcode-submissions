# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, preorder: List[int], inorder_map: dict, start : int, end : int) -> Optional[TreeNode]:
        if(start>end):
            return None
        
        rootVal = preorder[self.idx]

        i = inorder_map[rootVal]

        self.idx+=1
        
        root = TreeNode(rootVal)
        root.left = self.solve(preorder,inorder_map,start,i-1)
        root.right = self.solve(preorder,inorder_map,i+1,end)
        return root 

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        self.idx = 0 
        inorder_map = {}
        for idx,val in enumerate(inorder):
            inorder_map[val] = idx
        return self.solve(preorder,inorder_map,0,n-1)