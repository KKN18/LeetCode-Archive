class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _max = 0
        _min = 0
        ans = 0
        for x in nums:
            _max = max(_max + x, 0)
            _min = min(_min + x, 0)
            ans = max(_max, -_min, ans)
        return ans