class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numGroup = len(hand)//groupSize
        dic = {}
        if len(hand) % groupSize != 0:
            return False
        for p in range(len(hand)):
            if(hand[p] in dic):
                dic[hand[p]] += 1
            else:
                dic[hand[p]] = 1
        for i in range(numGroup):
            minn = min(dic)
            if(dic[minn] == 0):
                del(dic[minn])
            for j in range(groupSize):
                n = minn + j
                if dic.get(n, 0) == 0:
                    return False
                dic[n] -= 1
                if dic[n] == 0:
                    del dic[n]

        return True

            

