class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*(len(temperatures))
        stack=[]
        r=0
        for o,i in enumerate(temperatures):
            if len(stack)>0:
                while len(stack)!=0 and i>stack[-1][1] :
                    oind,ovalue= stack.pop()
                    print(oind,ovalue)
                    res[oind]= o-oind
            stack.append((o,i))
            r=o
        l=len(temperatures)-1
    
        return res
        #hold tuple of index of where originally in array and subtract by i. Array will always be decreasing
    