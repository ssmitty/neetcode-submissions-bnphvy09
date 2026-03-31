# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q=0
        curr=head
        while(curr):
            curr=curr.next
            q+=1
        first=head
        i=0
        if q==1:
            curr=None
            return curr
        if i==q-n:
            first=first.next
            return first
        while i+1!=q-n:
            first=first.next
            i+=1   
        first.next=first.next.next
        return head

        
        
