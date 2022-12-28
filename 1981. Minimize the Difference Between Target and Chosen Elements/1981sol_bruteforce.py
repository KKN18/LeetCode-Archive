class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        num_row = len(mat)
        num_col = len(mat[0])

        min_sum = sum(min(row) for row in mat)
        if min_sum > target:
            return min_sum - target
        
        max_sum = sum(max(row) for row in mat)
        if max_sum < target:
            return target - max_sum
        


        sum_list = [0]
        for row in mat:
            sum_list = [item + num for item in sum_list for num in row if item + num <= 2*target-min_sum]
        # print(f"sum_list : {sum_list}")
        ans = min(abs(x - target) for x in sum_list)
        return ans