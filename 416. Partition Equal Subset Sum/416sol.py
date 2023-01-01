class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _len = len(nums)
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        dp = [False for i in range(target+1)]
        dp[0] = True
        
        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i] == False:
                    if dp[i-num] == True:
                        dp[i] = True
                
        return dp[target]
                
              