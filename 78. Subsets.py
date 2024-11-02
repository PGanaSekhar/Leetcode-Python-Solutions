class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r=[[]]
        for i in range(1,len(nums)+1):
            for j in list(combinations(nums,i)):
                r.append(list(j))
        return r
