# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a,b=head,None
        while a:
            if a.val==val:
                if b:
                    b.next=a.next
                else:
                    head=a.next
                a=a.next
            else:
                a,b=a.next,a
        return head
