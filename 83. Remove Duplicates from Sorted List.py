# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b,c=head,None
        while b:
            if b.val in a:
                c.next=b.next      
            else:
                a.append(b.val)
                c=b
            b=b.next
        return head
