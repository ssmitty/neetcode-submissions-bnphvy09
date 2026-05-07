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
            print(hashet)
            if curr not in hashet:
                hashet[curr]=1
                curr=curr.next
            else:
                print(curr)
                return True
        return False

        