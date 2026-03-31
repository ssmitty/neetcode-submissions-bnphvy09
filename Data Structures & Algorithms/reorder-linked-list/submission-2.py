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
        slowly=slow.next
        slow.next=None
        while slowly:
            temp=slowly.next
            slowly.next=prev
            prev=slowly
            slowly=temp
        new=head
        while prev:
            tmpn=new.next
            tmpp=prev.next
            new.next=prev
            prev.next=tmpn
            new=tmpn
            prev=tmpp

        
        

            
        
      