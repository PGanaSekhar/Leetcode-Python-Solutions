class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        a=Counter(nums1)
        b=Counter(nums2)
        for i in set(nums1).intersection(nums2):
            r.extend([i]*min(a[i],b[i]))
        return r
