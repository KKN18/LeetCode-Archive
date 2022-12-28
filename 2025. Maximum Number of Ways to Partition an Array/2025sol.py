class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = len(answerKey)
        maxCount = 0
        kf = k
        j = 0
        for i in range(length):
            if answerKey[i] == 'F':
                kf -= 1
            if kf < 0:
                while kf < 0:
                    if answerKey[j] == 'F':
                        kf += 1
                    j += 1
            maxCount = max(maxCount, i - j + 1)
                
        kt = k
        j = 0
        for i in range(length):
            if answerKey[i] == 'T':
                kt -= 1
            if kt < 0:
                while kt < 0:
                    if answerKey[j] == 'T':
                        kt += 1
                    j += 1
            maxCount = max(maxCount, i - j + 1)
                
        
        return maxCount