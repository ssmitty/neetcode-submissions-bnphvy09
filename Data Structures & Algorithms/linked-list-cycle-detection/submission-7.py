# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset={}
        curr=head
        i=1
    
        while(curr):

            if curr in hashset :
                return True
            else:
                hashset[curr]=i
                curr=curr.next
                i+=1
        return False
        