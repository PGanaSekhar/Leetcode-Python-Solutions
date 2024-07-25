# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a=head
        b=head.next
        while b and b.next:
            a=a.next
            b=b.next.next
        t=a.next
        a.next=None
        p=None
        while t:
            g=t.next
            t.next=p
            p=t
            t=g
        f1=head
        f2=p
        while f2:
            t1,t2=f1.next,f2.next
            f1.next=f2
            f2.next=t1
            f1=t1
            f2=t2
