# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        s=head
        f=head
        while f:
            if f.next:
                f=f.next.next
                t=s
                s=s.next
            else:
                break
        t.next=s.next
        return head
