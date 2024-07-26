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
        a={None:None}
        t=head
        while t:
            c=Node(t.val)
            a[t]=c
            t=t.next
        t=head
        while t:
            c=a[t]
            c.next=a[t.next]
            c.random=a[t.random]
            t=t.next
        return a[head]
