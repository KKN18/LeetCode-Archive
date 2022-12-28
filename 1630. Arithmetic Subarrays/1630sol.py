class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        numAnswer = len(l)
        ansList = [False for i in range(numAnswer)]
        for i in range(numAnswer):
            subList = nums[l[i]:r[i]+1]
            subList = sorted(subList)
            print(subList)
            prevDiff = subList[0] - subList[1]
            ans = True
            for j in range(1, len(subList)-1):
                curDiff = subList[j] - subList[j+1]
                print(curDiff)
                if curDiff != prevDiff:
                    ans = False
            ansList[i] = ans
        return ansList