# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        newlist=ListNode()
        newlist1=newlist
        mapping={}
        while l1 and l2:
            if l1.val<l2.val:
                newlist1.next=ListNode(l1.val)
                l1=l1.next
            else:
                newlist1.next=ListNode(l2.val)
                l2=l2.next
            print(newlist.val)
            newlist1=newlist1.next
        while l1:
            newlist1.next=ListNode(l1.val)
            l1=l1.next
            newlist1=newlist1.next
        while l2:
            newlist1.next=ListNode(l2.val)
            l2=l2.next
            newlist1=newlist1.next
        return newlist.next