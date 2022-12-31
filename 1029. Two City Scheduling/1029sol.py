class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aDiffs = []
        bDiffs = []
        halfLength = len(costs) // 2
        totalCost = 0
        aCount = 0
        for i, cost in enumerate(costs):
            e1, e2 = cost
            if e1 < e2:
                totalCost += e1
                aCount += 1
                aDiffs.append([i, e2 - e1])
            else:
                totalCost += e2
                bDiffs.append([i, e1 - e2])
        
        if aCount == halfLength:
            return totalCost
        elif aCount < halfLength:
            bDiffs = sorted(bDiffs, key = lambda x:x[1])
            for i in range(halfLength - aCount):
                totalCost += bDiffs[i][1]
        else:
            aDiffs = sorted(aDiffs, key = lambda x:x[1])
            for i in range(aCount - halfLength):
                totalCost += aDiffs[i][1]
        return totalCost
                