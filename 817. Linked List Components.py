# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        r=0
        f=0
        while head:
            if head.val in nums and f==0:
                r+=1
                f+=1
            elif head.val in nums:
                f+=1
            else: f=0
            head=head.next
        return r
