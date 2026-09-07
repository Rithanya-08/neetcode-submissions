# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = []
        queue2 = []

        queue1.append(p)
        queue2.append(q)
        
        while(queue1 or queue2):
            ele1 = queue1.pop(0)
            ele2 = queue2.pop(0)
            if(ele1 == None and ele2 == None):
                continue
            if(ele1 == None or ele2 == None):
                return False

            if(ele1.val != ele2.val):
                return False

            if(ele1.left):
                queue1.append(ele1.left)
            else:
                queue1.append(None)
            if(ele1.right):
                queue1.append(ele1.right)
            else:
                queue1.append(None)
            
            if(ele2.left):
                queue2.append(ele2.left)
            else:
                queue2.append(None)
            if(ele2.right):
                queue2.append(ele2.right)
            else:
                queue2.append(None)

        return True
        