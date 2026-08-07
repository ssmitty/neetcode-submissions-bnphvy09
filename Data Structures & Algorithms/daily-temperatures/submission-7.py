class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[[0,temperatures[0]]]
        i=1
        res=[0]*len(temperatures)
        while i<len(temperatures):
            while len(stack)>0 and temperatures[i]>stack[-1][1]:
                ind,val=stack.pop()
                res[ind]=i-ind
            else:
                stack.append([i,temperatures[i]])
            i+=1
        return res
