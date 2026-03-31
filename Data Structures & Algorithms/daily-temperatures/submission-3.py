class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[(0,temperatures[0])]
        for i in range(1,len(temperatures)):
            while len(stack)!=0 and temperatures[i]>stack[-1][1]:
                ind,temp=stack.pop()
                res[ind]=i-ind
            stack.append([i,temperatures[i]])
            print(stack[0][1])
        return res