# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        def merging(l1,l2):
            g=ListNode()
            b=g
            while l1 and l2:
                if l1.val<l2.val:
                    b.next=l1
                    b=b.next
                    l1=l1.next
                else:
                    b.next=l2
                    b=b.next
                    l2=l2.next
            if l1:
                b.next=l1
            if l2:
                b.next=l2
            return g.next

        while len(lists)>1:
            a=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                a.append(merging(l1,l2))
            lists=a
        return lists[0]
