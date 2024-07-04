# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        while a.next:
            if a.val==0:
                b=a.next
                t=0
                while b.val!=0:
                    t+=b.val
                    b=b.next
                a.val=t
                if b.next:
                    a.next=b
                else:
                    a.next=b.next
                    break
            a=a.next
        return head
