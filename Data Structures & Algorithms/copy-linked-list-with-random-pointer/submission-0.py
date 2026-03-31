"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has={None:None}
        curr=head
        while curr:
            new=Node(curr.val)
            has[curr]=new
            curr=curr.next
        curr=head
        while curr:
            newc= has[curr]
            newc.next=has[curr.next]
            newc.random=has[curr.random] 
            curr=curr.next   
        return has[head]