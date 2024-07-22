class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        r=[]
        a=dict(sorted(a.items(),key=lambda x:x[1],reverse=True))
        for i,j in a.items():
                r.append(i)
                if len(r)==k:
                    return r
