# Definition for singly-linked list.
    #class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #elf.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            print("here")
            temp=curr.next
            curr.next=prev
            print(curr.val)
            prev=curr
            curr=temp

            
            
        return prev
        
            
