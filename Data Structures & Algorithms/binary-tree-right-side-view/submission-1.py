# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        queue = []
        result = []

        queue.append(root)

        while(queue):
            l = len(queue)
            curr = []
            for i in range(l):
                ele = queue.pop(0)
                curr.append(ele)
                if(ele.left):
                    queue.append(ele.left)
                if(ele.right):
                    queue.append(ele.right)
                
            n = curr.pop()
            result.append(n.val)

        return result