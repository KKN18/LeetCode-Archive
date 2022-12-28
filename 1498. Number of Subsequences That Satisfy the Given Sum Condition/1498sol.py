class Solution:
    def numSubseq(self, A, target: int) -> int:
        length = len(A)
        A.sort()
        count = 0
        for i in range(length):
            x = A[i]
            l = i+1
            r = length-1
            idx = -1
            while(l<=r):
                mid = (l+r)//2
                val_mid = A[mid]
                if x + val_mid <= target:
                    l = mid + 1
                    idx = mid
                else:
                    r = mid - 1
            if idx != -1:
                count += (1 << (idx - i))
                # print(i, idx, count)
            else:
                if x * 2 <= target:
                    count += 1
        return count % (10**9+7)