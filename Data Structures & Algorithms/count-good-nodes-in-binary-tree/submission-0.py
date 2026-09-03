# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if(root == None):
            return 0

        stack = []
        stack.append((root,root.val))
        result = 0
        maxx = 0

        while(stack):
            el,maxx = stack.pop()
            if(el.val>=maxx):
                result += 1
            new_maxx = max(el.val,maxx)
            if(el.left):
                stack.append((el.left,new_maxx))
            if(el.right):
                stack.append((el.right,new_maxx))

        return result