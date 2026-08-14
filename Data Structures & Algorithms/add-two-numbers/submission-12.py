# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=ListNode()
        dummy=newlist
        while l1 and l2:
            if l1.val+l2.val>=10:
                newlist.next=ListNode(l1.val+l2.val-10)
                if l1.next:
                    l1.next.val+=1
                elif l2.next:
                    l2.next.val+=1
                else:
                    newlist=newlist.next
                    newlist.next=ListNode(1)
                    return dummy.next
                newlist=newlist.next
            else:
                newlist.next=ListNode(l1.val+l2.val)
                newlist=newlist.next
            l1=l1.next
            l2=l2.next
        while l1:
            if l1.val>=10 and l1.next==None:
                newlist.next=ListNode(l1.val-10)
                newlist=newlist.next
                newlist.next=ListNode(1)
                return dummy.next
            elif l1.val>=10:
                print(l1.val)
                newlist.next=ListNode(l1.val-10)
                l1.next.val+=1
                newlist=newlist.next
                l1=l1.next
            else:
                newlist.next=ListNode(l1.val)
                newlist=newlist.next
                l1=l1.next
        while l2:
            if l2.val>=10 and l2.next==None:
                newlist.next=ListNode(l2.val-10)
                newlist=newlist.next
                newlist.next=ListNode(1)
                return dummy.next
            elif l2.val>=10:
                print(l2.val)
                newlist.next=ListNode(l2.val-10)
                l2.next.val+=1
                newlist=newlist.next
                l2=l2.next
            else:
                newlist.next=ListNode(l2.val)
                newlist=newlist.next
                l2=l2.next
        return dummy.next
            
        