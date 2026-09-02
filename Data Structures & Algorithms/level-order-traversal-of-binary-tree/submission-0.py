# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []

        queue = []
        result = []

        queue.append(root)
        j = 0 


        while(queue):
            l = len(queue)
            curr = []
            
            for i in range(l):
                ele = queue.pop(0)
                curr.append(ele.val)
                if(ele.left):
                    queue.append(ele.left)
                if(ele.right):
                    queue.append(ele.right)
            result.append(curr)
        return result
