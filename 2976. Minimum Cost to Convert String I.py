class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        a=defaultdict(list)
        for i,j,k in zip(original,changed,cost):
            a[i].append((j,k))
        
        def dijkstra(s):
            heap=[(0,s)]
            min={}
            while heap:
                c,n=heapq.heappop(heap)
                if n in min:
                    continue
                min[n]=c
                for i,j in a[n]:
                    heapq.heappush(heap,(c+j,i))
            return min
        min_cost={c:dijkstra(c) for c in set(source)}
        r=0
        for i,j in zip(source,target):
            if j not in min_cost[i]:
                return -1
            else:
                r+=min_cost[i][j]
        return r
