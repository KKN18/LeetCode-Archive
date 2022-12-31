class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maxCount = 0
        print(nums)
        for i in range(len(nums)):
            idx = i
            count = 1
            num = nums[idx]
            while(idx < len(nums)):
                square = num ** 2
                left = i+1
                right = len(nums) - 1
                isFound = False
                while(left <= right):
                    mid = (left + right) // 2
                    val = nums[mid]
                    if square == val:
                        isFound = True
                        break
                    if square > val:
                        left = mid + 1
                    else:
                        right = mid - 1
                if isFound:
                    idx = mid
                    count += 1
                    num = square
                else:
                    break
            maxCount = max(maxCount, count)
        if maxCount == 1:
            return -1
        return maxCount
                