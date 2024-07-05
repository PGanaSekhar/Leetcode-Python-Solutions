# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        r=[]
        i=0
        while head.next.next:
            if (head.next.val>head.val and head.next.next.val<head.next.val) or (head.next.val<head.val and head.next.next.val>head.next.val):
                r.append(i)
            i+=1
            head=head.next
        if len(r)<2:
            return [-1,-1]
        if len(r)==2:
            a=r[1]-r[0]
            return [a,a]
        a=[]
        for i in range(len(r)-1):
            a.append(r[i+1]-r[i])
        return [min(a),r[-1]-r[0]]
