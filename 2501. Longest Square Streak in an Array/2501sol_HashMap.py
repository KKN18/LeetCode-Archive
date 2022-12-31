class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        _map = {}
        maxCount = 0
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            count = _map.get(num**2, 0) + 1
            _map[num] = count
            maxCount = max(maxCount, count)
        if maxCount == 1:
            return -1
        return maxCount