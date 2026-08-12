# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr= head
        while curr:
            tmp=prev
            tmp2=curr.next
            prev=curr
            prev.next=tmp
            curr=tmp2
            print(curr)
            
        return prev
        