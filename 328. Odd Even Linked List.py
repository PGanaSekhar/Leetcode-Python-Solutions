# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return head
        d=ListNode()
        e=ListNode()
        m=d
        n=e
        while head and head.next!=None:
            m.next=head
            m=m.next
            n.next=head.next
            n=n.next
            head=head.next.next
        if n.next:
            m.next=n.next
            n.next=None
            m.next.next=e.next
        else:
            m.next=e.next
        return d.next
