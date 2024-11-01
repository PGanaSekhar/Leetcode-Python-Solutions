# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=head
        while b:
            a.append(b.val)
            b=b.next
        a.sort()
        i=0
        g=head
        while g:
            g.val=a[i]
            i+=1
            g=g.next
        return head
