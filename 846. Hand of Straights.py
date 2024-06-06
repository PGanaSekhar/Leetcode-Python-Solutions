class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        g=groupSize
        h=0
        hand.sort()
        for i in range(len(hand)//g):
            t=[hand[h]+j in hand for j in range(g)]
            if False in t:
                return False
            else:
                a=hand[h]
                for j in range(g):
                    hand.remove(a+j)
        if len(hand)>=1:
            return False
        return True
