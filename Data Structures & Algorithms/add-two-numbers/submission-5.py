# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        while l1 and l2:
            if l1.val +l2.val>=10:
                tail.next=ListNode(l1.val+l2.val-10)
                if l1.next:
                    l1.next.val+=1
                elif l2.next:
                    l2.next.val+=1
                else:
                    tail=tail.next
                    tail.next=ListNode(1)
                tail=tail.next
            else:
                tail.next=ListNode(l1.val+l2.val)
                tail=tail.next
            l1=l1.next
            l2=l2.next
        while l1:
            if l1.val>=10:
                tail.next=ListNode(10-l1.val)
                if l1.next:
                    l1.next.val+=1
                else:
                    tail=tail.next
                    tail.next=ListNode(1)
                    break
            else:
                tail.next=ListNode(l1.val)
            tail=tail.next
            l1=l1.next
        while l2:
            if l2.val>=10:
                tail.next=ListNode(10-l2.val)
                if l2.next:
                    l2.next.val+=1
                else:
                    tail=tail.next
                    tail.next=ListNode(1)
                    break
            else:
                tail.next=ListNode(l2.val)
            tail=tail.next
            l2=l2.next
        return dummy.next