class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        num_row = len(mat)
        num_col = len(mat[0])
        
        dp = defaultdict(defaultdict)

        globalMin = float("inf")

        for i in range(num_row):
            mat[i] = sorted(mat[i])

        def minAbsDiff(row, prevSum):
            nonlocal globalMin
            if row == num_row:
                globalMin = min(globalMin, abs(prevSum - target))
                return abs(prevSum - target)
            
            if (row in dp) and (prevSum in dp[row]):
                return dp[row][prevSum]

            if prevSum - target > globalMin:
                return float("inf")

            minDiff = float("inf")
            for col in range(num_col):
                diff = minAbsDiff(row+1, prevSum+mat[row][col])
                if diff == 0:
                    minDiff = 0
                    break
                minDiff = min(diff, minDiff)
                
            dp[row][prevSum] = minDiff
            return minDiff
        return minAbsDiff(0, 0)