class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        _len = len(tops)
        vTop = [0] * 7
        vBot = [0] * 7
        vTotal = [_len] * 7
        
        for i in range(_len):
            cTop = tops[i]
            cBot = bottoms[i]
            if cTop == cBot:
                vTotal[cTop] -= 1
            else:
                vTop[cTop] += 1
                vBot[cBot] += 1

        _min = float('inf')
        pos = False
        for i in range(1, 7):
            if vTotal[i] == vTop[i] + vBot[i]:
                nRotate = min(vTop[i], vBot[i])
                _min = min(_min, nRotate)
                pos = True
        if pos == False:
            return -1
        return _min