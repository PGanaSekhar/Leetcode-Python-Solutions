class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        a=boxTypes
        c=0
        r=0
        for i in a:
            if c+i[0]>truckSize:
                r+=(truckSize-c)*i[1]
                break
            else:
                c+=i[0]
                r+=i[0]*i[1]
        return r
