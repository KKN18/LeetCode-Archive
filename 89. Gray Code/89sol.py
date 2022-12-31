class Solution:
    def grayCode(self, n: int) -> List[int]:
        strBits = ['0', '1']
        for i in range(n-1):
            tmp0 = ['0' + b for b in strBits]
            tmp1 = ['1' + b for b in strBits[::-1]]
            strBits = tmp0 + tmp1
        numBits = []
        for sb in strBits:
            numBits.append(int(sb, 2))
        return numBits