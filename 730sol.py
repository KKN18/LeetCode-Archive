class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0,temperatures[0])]
        ans = [0]*len(temperatures)
        i = 1
        for index,every in enumerate(temperatures[1:]):
            index+=1
            #print(stack)
            while stack and every > stack[-1][1]:
                ans[stack[-1][0]] =  index-stack[-1][0]
                stack.pop()
            stack.append((index,every))
        
        return ans
