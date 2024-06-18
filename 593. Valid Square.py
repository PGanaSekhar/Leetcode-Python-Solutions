class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p2==p2==p3==p4:
            return False
        def formula(p1,p2):
            return (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
        dist=[formula(p1,p2),formula(p2,p3),formula(p3,p4),formula(p4,p1),formula(p1,p3),formula(p2,p4)]
        dist.sort()
        if len(set(dist[:4]))==1:
            if dist[4]==dist[5]:
                return True
        return False
