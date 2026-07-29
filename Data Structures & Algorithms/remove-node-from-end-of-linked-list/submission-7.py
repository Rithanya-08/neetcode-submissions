# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        if(head.next == None and n ==1 ):
            return None
        curr = dummy
        fast = dummy
        
        for i in range(n+1):
            fast = fast.next

        while(fast):
            curr = curr.next
            fast = fast.next

        curr.next = curr.next.next

        return dummy.next
