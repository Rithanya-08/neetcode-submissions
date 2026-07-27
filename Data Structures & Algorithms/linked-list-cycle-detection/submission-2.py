# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        first = True

        if(head == None):
            return False

        while(slow.next and fast.next and fast.next.next):
            if(slow == fast and first  == False):
                return True
            
            first = False

            slow = slow.next
            fast = fast.next.next

        return False
