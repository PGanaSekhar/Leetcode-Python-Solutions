# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        g=head
        a,b=head,None
        c=[]
        while g:
            c.append(g.val)
            g=g.next
        c=Counter(c)
        while a:
            if c[a.val]!=1:
                while a.next:
                    if a.next.val==a.val:
                        a=a.next
                    else: break
                if b:
                    b.next=a.next
                else:
                    head=a.next
                a=a.next
            else:
                a,b=a.next,a
        return head
