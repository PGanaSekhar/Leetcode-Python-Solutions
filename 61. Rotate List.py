# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while not head or not head.next:
            return head
        m=head
        a=[]
        l=0
        while m:
            a.append(m.val)
            m=m.next
            l+=1
        k=k%l
        a[:]=a[-k:]+a[:-k]
        i=0
        m=head
        while m:
            m.val=a[i]
            i+=1
            m=m.next
        return head
