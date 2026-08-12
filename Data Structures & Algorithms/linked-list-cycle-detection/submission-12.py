# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashet={}
        curr=head
        while curr:
            print(curr.val,hashet)
            print(curr,"Curr")
            if curr in hashet:
                return True
            hashet[curr]=curr.val
            curr=curr.next
        return False
        