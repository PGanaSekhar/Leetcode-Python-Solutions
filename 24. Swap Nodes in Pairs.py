# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        a=ListNode()
        b=a
        while temp:
            if temp.next:
                b.next=ListNode(temp.next.val)
                b.next.next=ListNode(temp.val)
                b=b.next.next
                temp=temp.next.next
            else:
                b.next=ListNode(temp.val)
                temp=temp.next
        return a.next
