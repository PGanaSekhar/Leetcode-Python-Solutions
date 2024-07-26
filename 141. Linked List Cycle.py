# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        b=head
        while b:
            if b in a:
                return True
            else:
                a.add(b)
            if b.next==None:
                return False
            b=b.next
