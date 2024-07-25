# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d=ListNode(0,head)
        r=d
        l=head
        while n>0 and l:
            l=l.next
            n-=1
        while r and l:
            r=r.next
            l=l.next
        r.next=r.next.next
        return d.next
