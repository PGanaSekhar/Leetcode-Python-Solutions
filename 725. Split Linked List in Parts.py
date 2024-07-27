# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        r=[None]*k
        a=head
        l=0
        while a:
            l+=1
            a=a.next
        if l<=k:
            a=head
            i=0
            while a:
                r[i]=ListNode(a.val)
                i+=1
                a=a.next
            return r
        else:
            g=l%k
            h=l//k
            a=head
            for i in range(k):
                t=0
                b=ListNode()
                j=b
                while t<h:
                    j.next=ListNode(a.val)
                    a=a.next
                    j=j.next
                    t+=1
                if g:
                    j.next=ListNode(a.val)
                    a=a.next
                    j=j.next
                    g-=1
                r[i]=b.next
            return r
