class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=list(set(edges[0]).intersection(set(edges[1])))
        return a[0]
