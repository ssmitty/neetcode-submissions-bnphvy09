# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow=fast=head
        
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next=None
        prev2=None
        temp3=slow

        while temp3:
            tmp=temp3.next
            temp3.next=prev2
            prev2=temp3
            temp3=tmp
        temp=head
        temp2=prev2
        dummy=ListNode()
        tail=dummy
        while temp and temp2:
            tail.next=temp
            temp=temp.next
            tail=tail.next
            tail.next=temp2
            temp2=temp2.next
            tail=tail.next
        
        