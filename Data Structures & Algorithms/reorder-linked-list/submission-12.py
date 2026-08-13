# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        sl=slow
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        dummy=node=ListNode()
        heady=head
        while prev and heady and prev!=heady:
            n1=heady.next
            n2=prev.next
            dummy.next=heady
            dummy=dummy.next
            dummy.next=prev
            dummy=dummy.next
            prev=n2
            heady=n1
        
        

        